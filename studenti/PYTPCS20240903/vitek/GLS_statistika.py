import pandas as pd
import folium
import requests
import csv


def get_coordinates(postal_code):
    """Získá zeměpisné souřadnice pro dané PSČ pomocí Nominatim.

    Args:
      postal_code: PSČ ve správném formátu pro danou zemi.

    Returns:
      Tuple obsahující zeměpisnou šířku a délku, nebo None, pokud se nepodařilo získat souřadnice.
    """

    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'format':         'json',
        'postalcode':     postal_code,
        'countrycodes':   'cz',
        'addressdetails': 1
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Zvedne výjimku, pokud je status kódu chybný

    if response.json():
        results = response.json()[0]
        lat = results['lat']
        lon = results['lon']
        return lat, lon
    else:
        return None


def get_souradnice(zipcode: int) -> []:
    """

    :param zipcode:
    :return: slovnik obsahujici zemepisnou delku a sirku
    """
    coordinates = get_coordinates(zipcode)
    if coordinates:
        latitude = float(coordinates[0])
        longitude = float(coordinates[1])
    else:
        latitude = ''
        longitude = ''
    return {'latitude': latitude, 'longitude': longitude}


def soucet_sloupce(sloupec: []) -> float:
    """
    
    :param sloupec: 
    :return: soucet vsech hodnot
    """
    suma = 0
    for cislo in sloupec:
        suma += cislo
    return round(suma, 2)


def pocet_baliku_bez_box(sloupec: []) -> int:
    """

    :param sloupec:
    :return: pocet standardnich baliku
    """
    pocet = 0
    for cislo in sloupec:
        if cislo != CENA_BOX:
            pocet += 1
    return pocet


def pocet_baliku_box(sloupec: []) -> int:
    """

    :param sloupec:
    :return: pocet baliku do boxu
    """
    pocet = 0
    for cislo in sloupec:
        if cislo == CENA_BOX:
            pocet += 1
    return pocet


def prumer_procento(reference: [], hodnota: []) -> float:
    """

    :param reference:
    :param hodnota:
    :return: prumer hodnoty v procentech dvou sloupcu bez zasilek do boxu
    """
    suma = 0
    poplatek = 0
    for index, cislo in enumerate(reference):
        if cislo != CENA_BOX:
            suma += cislo
            poplatek += hodnota[index]
    return round(poplatek / suma * 100, 2)


NAZEV_SOUBORU = 'SettlementDocument_24056685_55424.xlsx'
NAZEV_STATISTIKY = 'Statistika.csv'
NAZEV_MAPY = 'Mapa.html'
CENA_BOX = 40

# Nacteni excel souboru
df = pd.read_excel(NAZEV_SOUBORU, sheet_name=None)

statistika = []
sloupec_cena_celkem = df['Rozpis k doručení']['Celková cena / Total amount']
sloupec_cena_prepravy = df['Rozpis k doručení']['Cena přepravy / Transport fee']

statistika.append(['Celkova cena prepravy', soucet_sloupce(sloupec_cena_celkem)])
statistika.append(
    ['Prumerna cena za 1 balik', round(soucet_sloupce(sloupec_cena_celkem) / len(sloupec_cena_celkem), 2)])
statistika.append(
    ['Pocet standarnich baliku', pocet_baliku_bez_box(df['Rozpis k doručení']['Cena přepravy / Transport fee'])])
statistika.append(['Pocet baliku do boxu', pocet_baliku_box(sloupec_cena_prepravy)])
statistika.append(['Palivovy priplatek (%)',
                   prumer_procento(sloupec_cena_prepravy, df['Rozpis k doručení']['Palivový příplatek / Diesel fee'])])
statistika.append(['Mytny priplatek (%)',
                   prumer_procento(sloupec_cena_prepravy, df['Rozpis k doručení']['Mýtný příplatek / Toll fee'])])

# Nacteni PSC do slovniku
psc_seznam = {}
for prvek in df['Rozpis k doručení']['Adresa příjemce / Delivery address']:
    if prvek[0:2] == "CZ":
        key = int(prvek[3:8])
        psc_seznam[key] = ""

# Ke kazdemu PSC priradi GPS souradnice
with open('Databaze_PSC.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    psc_databaze = {}
    for radek in reader:
        psc_databaze[int(radek['psc'])] = {'latitude': radek['latitude'], 'longitude': radek['longitude']}

psc_seznam_nedohledane = {}
sluzba_nedostupna = False
for key in psc_seznam:
    if psc_databaze.get(key):
        psc_seznam[key] = psc_databaze[key]
    else:
        try:
            nove_souradnice = get_souradnice(key)
            psc_seznam[key] = nove_souradnice
            psc_databaze[key] = nove_souradnice
        except:
            sluzba_nedostupna = True
            psc_seznam_nedohledane[key] = ""
if sluzba_nedostupna:
    print("Sluzba na zjisteni GPS souradnic je nedostupna. Vysledky nejsou kompletni")
for key in psc_seznam_nedohledane:
    psc_seznam.pop(key)

with open('Databaze_PSC.csv', 'w') as file:
    soubor_na_zapsani = []
    for key in psc_databaze:
        soubor_na_zapsani.append(
            {'psc': key, 'latitude': psc_databaze[key]['latitude'], 'longitude': psc_databaze[key]['longitude']})
    fieldnames = ['psc', 'latitude', 'longitude']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(soubor_na_zapsani)

with open(NAZEV_STATISTIKY, 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(statistika)
print(f"Statistika byla ulozena do slozky s projektem pod nazvem {NAZEV_STATISTIKY}")

# Vytvoření základní mapy
map = folium.Map(location=[49.8, 15.3], zoom_start=8)
# pridani bodu na mapu
latitude = None
longitude = None
for misto in psc_seznam:
    latitude = psc_seznam[misto]['latitude']
    longitude = psc_seznam[misto]['longitude']
    if latitude and longitude:
        coord = (float(latitude), float(longitude))
    folium.Marker(coord, tooltip=misto).add_to(map)

# Uložení mapy
map.save(NAZEV_MAPY)
print(f"Mapa byla ulozena do slozky s projektem pod nazvem {NAZEV_MAPY}")
