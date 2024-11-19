"""

/home/pvlcek/data/kontakty.xls
c:\home\pvlcek\...

soubor = open("kontakty.xls")

r - cteni
w - vytvoreni/zapis
a - pridavam do souboru
b - binarnim rezimu   UTF-8

soubor.read()
soubor.write()

soubor.close()

pathlib     "adresar" / "podadresar" /mujsoubor.txt

soubor = open("data.txt", "r")
obsah = soubor.read()
# soubor.seek(0)
obsah = soubor.readlines()
soubor.close()
print(obsah)

vystup = open("zaloha.txt", "w")
#vystup.write(obsah)
vystup.writelines(obsah)
vystup.close()

"""
import csv


data_sloupce = ['jmeno', 'prijmeni', 'vek']

# kontextovy manazer with
# [Petr, VLcek, 30]
"""
with open("kontakty.txt", "r") as soubor:
    # provadim operace nad souborem
    for radek in soubor:
        # zpracovavam,e jednotlive radky samostatne
        radek_data = radek.strip().split(';')
        vizitka = {
            'jmeno': radek_data[0].capitalize(),
            'prijmeni': radek_data[1].capitalize(),
            'vek': int(radek_data[2])
        }
        print(vizitka)
print("--------------------------")


with open('kontakty.txt', 'r') as soubor:
    reader = csv.reader(soubor, delimiter=';')
    for radek in reader:
        print(radek)
print("--------------------------")
"""

with open('backup/kontakty.txt', 'r') as soubor:
    reader = csv.DictReader(soubor, delimiter=';', quotechar='"')
    for radek in reader:
        print(radek)


data = [
    ['jmeno', 'prijmeni', 'vek'],
    ['Pepa', 'Nos', 50],
    ['Alena', 'Ziva', 25]
]

with open('backup/kontakty_out.txt', 'w', newline='') as soubor:
    writer = csv.writer(soubor, delimiter=',')
    writer.writerows(data)

data_dict = [
    {'jmeno': 'petr', 'prijmeni': 'Vlcek', 'vek': '50'},
    {'jmeno': 'Pavel', 'prijmeni': 'vopiCka', 'vek': '40'},
    {'jmeno': 'Vera', 'prijmeni': 'Ziva, Novotna', 'vek': '25'},
]

with open('backup/kontakty_dict.txt', 'w', newline='') as soubor:
    writer = csv.DictWriter(soubor, delimiter=',', fieldnames=data_sloupce)
    writer.writeheader()
    writer.writerows(data_dict)

