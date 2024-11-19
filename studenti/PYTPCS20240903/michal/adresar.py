import csv


def nacist_kontakty_csv(soubor, delimiter=','):
    """Načte kontakty z CSV souboru do databáze a provede potřebné úpravy dat."""
    databaze = []
    try:
        with open(soubor, 'r', newline='') as soubor_csv:
            fieldnames = ['jmeno', 'prijmeni', 'rozliseni', 'email', 'telefon']
            reader = csv.DictReader(soubor_csv, delimiter=delimiter)
            for radek in reader:
                print(radek)
                # Formátování a úprava dat
                radek['jmeno'] = radek['jmeno'].strip().title()
                radek['prijmeni'] = radek['prijmeni'].strip().title()
                radek['email'] = radek['email'].strip().lower()
                radek['telefon'] = radek['telefon'].strip().replace(' ', '')
                radek['rozliseni'] = radek['rozliseni'].strip()

                # Validace emailu
                if '@' not in radek['email']:
                    print(f"Neplatný kontakt: {radek['jmeno']} {radek['prijmeni']} (neplatný e-mail).")
                    continue

                # Validace telefonu
                if not radek['telefon'].startswith('+') or not radek['telefon'][1:].isdigit():
                    print(f"Neplatný kontakt: {radek['jmeno']} {radek['prijmeni']} (nesprávný formát tel. čísla). ")
                    continue

                databaze.append(radek)
        print(f"Načteno {len(databaze)} kontaktů.")
    except FileNotFoundError:
        print(f"Soubor {soubor} nebyl nalezen.")
    return databaze


def ulozit_kontakty_csv(soubor, databaze):
    """Uloží aktuální databázi kontaktů do CSV souboru."""
    with open(soubor, 'w', newline='') as soubor_csv:
        fieldnames = ['jmeno', 'prijmeni', 'rozliseni', 'email', 'telefon']
        writer = csv.DictWriter(soubor_csv, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(databaze)
    print(f"Uloženo {len(databaze)} kontaktů do souboru {soubor}.")


def setridit_kontakty(databaze):
    """Seřadí kontakty podle příjmení a jména."""
    return sorted(databaze, key=lambda k: (k['prijmeni'], k['jmeno']))


def vytvorit_kontakt(databaze, jmeno, prijmeni, email, telefon, rozliseni=''):
    """Vytvoří nový kontakt a přidá ho do databáze, pokud už neexistuje."""
    jmeno = jmeno.strip().title()
    prijmeni = prijmeni.strip().title()
    email = email.strip().lower()
    telefon = telefon.strip().replace(' ', '')
    rozliseni = rozliseni.strip()

    for kontakt in databaze:
        if kontakt['jmeno'] == jmeno and kontakt['prijmeni'] == prijmeni and kontakt['rozliseni'] == rozliseni:
            return "Kontakt již existuje!"

    # Ověření platnosti emailu
    if '@' not in email:
        return "Neplatný email!"

    # Ověření platnosti telefonního čísla
    if not telefon.startswith('+') or not telefon[1:].isdigit():
        return "Neplatný formát telefonního čísla!"

    novy_kontakt = {
        'jmeno': jmeno,
        'prijmeni': prijmeni,
        'rozliseni': rozliseni,
        'email': email,
        'telefon': telefon
    }
    databaze.append(novy_kontakt)
    return "Kontakt byl úspěšně přidán."


def smazat_kontakt(databaze, jmeno, prijmeni, rozliseni=''):
    """Smaže kontakt z databáze na základě zadaných údajů."""
    jmeno = jmeno.strip().lower()
    prijmeni = prijmeni.strip().lower()
    rozliseni = rozliseni.strip().lower()

    for index, kontakt in enumerate(databaze):
        if (kontakt['jmeno'].lower() == jmeno and kontakt['prijmeni'].lower() == prijmeni and
                kontakt['rozliseni'].lower() == rozliseni):
            del databaze[index]
            return f"Kontakt {jmeno.title()} {prijmeni.title()} byl smazán."
    return "Kontakt nenalezen."


def najit_kontakt(databaze, jmeno='', prijmeni='', rozliseni='', email='', telefon=''):
    """Najde kontakt v databázi na základě zadaných údajů."""
    nalezene = []
    for kontakt in databaze:
        if (jmeno.lower() in kontakt['jmeno'].lower() or not jmeno) and \
                (prijmeni.lower() in kontakt['prijmeni'].lower() or not prijmeni) and \
                (rozliseni.lower() in kontakt['rozliseni'].lower() or not rozliseni) and \
                (email.lower() in kontakt['email'].lower() or not email) and \
                (telefon in kontakt['telefon'] or not telefon):
            nalezene.append(kontakt)
    return nalezene


def detail_kontaktu(kontakt):
    """Vrátí detail kontaktu"""
    return f"""
-----------------------------------------
| Jméno:     | {kontakt['jmeno']:<24} |
| Příjmení:  | {kontakt['prijmeni']:<24} |
| Rozlišení: | {kontakt['rozliseni']:<24} |
| Email:     | {kontakt['email']:<24} |
| Telefon:   | {kontakt['telefon']:<24} |
-----------------------------------------
"""


def hlavni_menu():
    """Hlavní uživatelské menu programu."""
    databaze = []
    while True:
        print()
        print("Adresář kontaktů - Hlavní menu:")
        print("1 - Načíst kontakty z CSV")
        print("2 - Uložit kontakty do CSV")
        print("3 - Vytvořit nový kontakt")
        print("4 - Seřadit kontakty")
        print("5 - Smazat kontakt")
        print("6 - Najít kontakt")
        print("7 - Vypsat všechny kontakty")
        print("H - Nápověda")
        print("Q - Konec programu")
        print()
        volba = input("Zadejte volbu: ").upper()

        if volba == '1':
            # Načtu kontakty z CSV
            databaze = nacist_kontakty_csv('databanka.csv')
        elif volba == '2':
            # Uložím kontakty do CSV
            ulozit_kontakty_csv('kontakty.csv', databaze)
        elif volba == '3':
            # Vytvořím nový kontakt
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            rozliseni = input("Zadejte rozlišení (nepovinné): ")
            email = input("Zadejte email: ")
            telefon = input("Zadejte telefon (+420...): ")
            print(vytvorit_kontakt(databaze, jmeno, prijmeni, email, telefon, rozliseni))
        elif volba == '4':
            # Seřadím kontakty
            databaze = setridit_kontakty(databaze)
            print("Kontakty byly seřazeny.")
        elif volba == '5':
            # Smažu kontakt
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            rozliseni = input("Zadejte rozlišení (nepovinné): ")
            print(smazat_kontakt(databaze, jmeno, prijmeni, rozliseni))
        elif volba == '6':
            # Najdu kontakt
            jmeno = input("Zadejte jméno (nepovinné): ")
            prijmeni = input("Zadejte příjmení (nepovinné): ")
            rozliseni = input("Zadejte rozlišení (nepovinné): ")
            email = input("Zadejte email (nepovinné): ")
            telefon = input("Zadejte telefon (nepovinné): ")
            nalezene = najit_kontakt(databaze, jmeno, prijmeni, rozliseni, email, telefon)
            if nalezene:
                print(f"Nalezeno {len(nalezene)} kontaktů:")
                for kontakt in nalezene:
                    print(detail_kontaktu(kontakt))
            else:
                print("Žádné kontakty nenalezeny.")
        elif volba == '7':
            # Vypíšu všechny kontakty
            for kontakt in databaze:
                print(detail_kontaktu(kontakt))
        elif volba == 'H':
            # Nápověda
            print("Adresář kontaktů - Nápověda:")
            print("1 - Načíst kontakty z CSV")
            print("2 - Uložit kontakty do CSV")
            print("3 - Vytvořit nový kontakt")
            print("4 - Seřadit kontakty")
            print("5 - Smazat kontakt")
            print("6 - Najít kontakt")
            print("7 - Vypsat všechny kontakty")
            print("H - Nápověda")
            print("Q - Konec programu")
        elif volba == 'Q':
            print("Ukončuji program.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.")


if __name__ == "__main__":
    hlavni_menu()
