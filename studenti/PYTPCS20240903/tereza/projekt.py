"""
Program, který bere v potaz pořizovací hodnotu, zůstatkovou hodnotu a další různé proměnné
Vypočítává, zdali se zařízení má rovnou vyměnit, je to na individuálním posouzení nebo neproběhne
Poté ukládá historii do souboru json

"""
import json

def ulozit_data(data, filename="historie.json"):
    """
    Uklada historii do souboru formatu JSON, pokud soubor neexistuje, vytvori ho.
    :param data: slovnik obsahujici zadanne hodnoty a vysledek vypoctu
    :param filename: nazev souboru
    :return:
    """
    try:
        with open(filename, "r") as file:
            historie = json.load(file)
    except FileNotFoundError:   # pokud neexistuje, vytvori se novy seznam
        historie = []

    historie.append(data)

    with open(filename, "w") as file:
        json.dump(historie, file, indent=4)

def rovnice(cenova_nabidka: int, naklady_na_servis: int, stari_stroje: int, zustatkova_hodnota: int, porizovaci_cena: int):
    """
    Funkce spocita vysledek, ktery se pouziva pro rozhodnuti, zda ma byt zarizeni vymeneno, opraveno
    nebo predano na individualni posouzeni na zaklade zadanych parametru. Vysledkem je cislo,
    ktere je dale vyhodnoceno.
    :param cenova_nabidka: Cena nabidnuta za opravu zarizeni
    :param naklady_na_servis: Celkove naklady na servis zarizeni
    :param stari_stroje: Stari stroje v mesicich
    :param zustatkova_hodnota: Zustatkova hodnota stroje (zbytkova hodnota odpisu)
    :param porizovaci_cena: Porizovaci cena zarizeni - jako jedina je fixni a uzivatel ji nezadava
    :return: Vypocet vysledku pro rozhodnuti o oprave nebo vymene
    """

    ers = cenova_nabidka + naklady_na_servis    # soucet nakladu na opravu stroje bez vymeny
    kpc = porizovaci_cena * 0.2     # koeficient porizovaci ceny
    tbo = 0 if stari_stroje < 60 else (stari_stroje - 60) / 3   # porovnava, zdali se stroj odepisuje, pokud ne, je vetsi sance, ze se stroj musi vymenit
    ezh = (zustatkova_hodnota / porizovaci_cena * 1) * 100  # zustatkova hodnota vyjadrena jako procento porizovaci ceny
    vysledek = (ers - kpc) + tbo - ezh  # vysledny vypocet
    return vysledek



def vyhodnoceni(vysledek: float):
    """
    Vyhodnoti, zda probehne vymena zarizeni na zaklade vysledku v predchozi funkci rovnice.
    Na zaklade vysledku poskytne doporuceni.
    :param vysledek: Vysledek vypoctu z funkce rovnice
    :return:
    """
    vysledek = round(vysledek,2)    #zaokrouhli vysledek na 2 desetinna mista
    if vysledek > 10:
        print(f"Replacement proběhne, oprava je nákladná. Výsledek rovnice je {vysledek}.")
    elif -10 < vysledek < 10:
        print(f"Je to na individuálním posouzení, výsledek rovnice je {vysledek}")
    else:
        print(f"Replacement neproběhne, zařízení je buďto nové nebo je oprava výhodná. Výsledek rovnice je {vysledek}")

def get_valid_input(prompt, valid_options=None):
    """
    Ziska validni vstup od uzivatele, pokud jsou zadany platne moznosti, kontroluje je
    :param prompt: zprava zobrazena uzivateli pri dotazu na vstup
    :param valid_options: Seznam platnych ciselnych hodnot od uzivatele. (Cislo zarizeni ve sloviku nize)
    :return:
    """
    while True:
        try:
            value = int(input(prompt))
            if valid_options and value not in valid_options:
                print(f"Prosím, vyberte jednu z možností: {valid_options}")
            else:
                return value
        except ValueError:
            print("Neplatný vstup, prosím zadejte číslo.")


def main():
    """
    Hlavni funkce programu, ktera ridi vyber zarizeni, sber vstupu a vypocty.
    Nakonec vysledek ulozi do souboru.
    Nabizi opakovane provedeni vypoctu, dokud uzivatel nezvoli ukonceni.
    """

    # slovnik zarizeni pro vyber uzivatelem, id: (nazev zarizeni, porizovaci cena)
    zarizeni = {
        1: ('Holding', 140),
        2: ('Pračka', 70),
        3: ('Myčka', 160),
        4: ('Lednice', 40),
        5: ('Toaster', 55),
        6: ('Spust na sendviče', 125),
        7: ('Příruční mrazák', 83),
        8: ('Konvektomat', 147),
        9: ('Kontaktní gril', 52),
        10: ('Hranolková stanice', 107),
        11: ('Hranolková fritéza', 227),
        12: ('Display', 138),
        13: ('Ledovač', 24),
        14: ('Tlaková fritéza', 335),
        15: ('Obalovací stůl', 190),
        16: ('Otevřená fritéza', 370),
        17: ('Marinator', 32),
        18: ('Shake', 145)
    }

    while True:
        print("\nVítejte v aplikaci Replacement")
        print("Vyberte porouchané zařízení:")
        for key, (name, _) in zarizeni.items():
            print(f"{key}. {name}")

        # ziskani vyberu zarizeni od uzivatele
        typ_zarizeni = get_valid_input("Zadejte číslo zařízení: ", valid_options=zarizeni.keys())

        # ziskani dalsich vstupu od uzivatele
        stari_stroje = get_valid_input("Zadejte stáří stroje v měsících:\n")
        print("V nasledujících krocích doplňte hodnotu v tisících bez nul.")
        print("(Například pokud je cenová nabídka 2 000, doplňte 2)")
        cenova_nabidka = get_valid_input("Zadejte hodnotu poslední cenové nabídky:\n")
        naklady_na_servis = get_valid_input("Zadejte náklady na servis:\n")
        zustatkova_hodnota = get_valid_input("Zadejte zůstatkovou hodnotu:\n")

        # shrnuti zadanych hodnot
        print(f"Shrnutí zadaných údajů:\n"
              f"Typ zařízení: {zarizeni[typ_zarizeni][0]}\n"
              f"Pořizovací cena: {zarizeni[typ_zarizeni][1]} 000\n"
              f"Cenová nabídka: {cenova_nabidka} 000\n"
              f"Náklady na servis: {naklady_na_servis} 000\n"
              f"Zůstatková hodnota odpisů: {0 if zustatkova_hodnota == 0 else f'{zustatkova_hodnota} 000'}")

        # shrnuti zustatkove hodnoty
        """
        if zustatkova_hodnota == 0:
            print("Zůstatková hodnota: 0")
        else:
            print(f"Zůstatková hodnota: {zustatkova_hodnota} 000")
        """
        print(f"Vyhodnocení na základě zadaných hodnot:\n")

        # porizovaci cena na zaklade vyberu zarizeni
        porizovaci_cena = zarizeni[typ_zarizeni][1]

        # vypocet rovnice a vyhodnoceni vysledku
        vysledek = rovnice(cenova_nabidka, naklady_na_servis, stari_stroje, zustatkova_hodnota, porizovaci_cena)
        vyhodnoceni(vysledek)

        # ulozeni vysledku do souboru
        data = {
            "typ_zarizeni": typ_zarizeni,
            "stari_stroje": stari_stroje,
            "cenova_nabidka": cenova_nabidka,
            "naklady_na_servis": naklady_na_servis,
            "zustatkova_hodnota": zustatkova_hodnota,
            "vysledek": vysledek
        }
        ulozit_data(data)


        # moznost provedeni dalsiho vypoctu
        opakovat = input("\nChcete provést další výpočet? (ano/ne): ").strip().lower()
        if opakovat != 'ano':
            print("Děkujeme za použití aplikace Replacement.")
            break


if __name__ == "__main__":
    """Spusteni programu"""
    main()
