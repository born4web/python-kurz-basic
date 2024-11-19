def adresar():
    print("""Vítejte v našem adresáři kontaktů.

Vyberte si, co chcete s kontakty udělat:
    1)  Načíst kontakty.
    2)  Uložit kontakty.
    3)  Setřídit kontakty.
    4)  Vytvořit kontakt.
    5)  Smazat kontakt.
    6)  Najít kontakt.
    7)  Detail kontaktu.
    8)  Vypsat kontakty.
    9)  Upravit kontakt.
    10) Home - návrat do nabídky.

""")

def jedna(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    soubor.close()

def dva(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","w")
    soubor.write("jmeno, prijmeni, rozliseni, email, telefon")
    soubor.close()

def tri(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    soubor.sort("jmeno, prijmeni, rozliseni, email, telefon")
    soubor.close()

def ctyri(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    soubor.append("jmeno, prijmeni, rozliseni, email, telefon")
    soubor.close()

def pet(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    soubor.remove("jmeno, prijmeni, rozliseni, email, telefon")
    soubor.close()

def sest(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    for kontakt in kontakty:
        if kontakt (jmeno, prijmeni, rozliseni, email, telefon) == jmeno, prijmeni, rozliseni, email, telefon:
            return kontakt
        return None
    soubor.close()

def sedm(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    print("--------------------------")
    soubor.print("! Jméno:      !" {jmeno}"                !")
    soubor.print("! Příjmení:   !" {prijmeni} "            !")
    soubor.print("! Rozlišení:  !" {rozliseni} "           !")
    soubor.print("! Telefon:    !" {telefon}"              !")
    soubor.print("! Email:      !" {email}"                !")
    print("--------------------------")
    soubor.close()

def osm(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    soubor.write("")
    soubor.close()

def devet[jmeno, prijmeni, rozliseni, email, telefon]:
       with open("C:\\adresar.csv", "r") as soubor:
            for radek in soubor:
           detail_kontaktu = radek.strip().split(';')
            vypsat_kontakty = {
                'jmeno': detail_kontaktu[0].capitalize(),
                'prijmeni': detail_kontaktu[1].capitalize(),
                'rozliseni': detail_kontaktu[2].capitalize(),
                'telefon': detail_kontaktu[4].capitalize(),
                'email': detail_kontaktu[5].capitalize(),
            }
            print(vypsat_kontakty)

def deset(jmeno, prijmeni, rozliseni, email, telefon):
    soubor = open("C:\\adresar.csv","a")
    soubor.write("")
    soubor.close()

volba = "nic"
while volba <> "10":
    adresar()
    volba = input ("Vaše volba? (1,2,3,4,5,6,7,8,9,10)")

    if volba == "1"
    jedna(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "2"
    dva(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "3"
    tri(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "4"
    ctyri(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "5"
    pet(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "6"
    sest(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "7"
    sedm(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "8"
    osm(jmeno, prijmeni, rozliseni, email, telefon)

    elif volba == "9"
    devet(jmeno, prijmeni, rozliseni, email, telefon)

    else volba == "10"
        pass
