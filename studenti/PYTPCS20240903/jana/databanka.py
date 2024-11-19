import csv

kontakty = []


def nacist_kontakty(soubor):
    """Prida kazdy radek jako slovnik do seznamu"""
    with open(soubor, 'r') as file:
        reader = csv.DictReader(file, delimiter=',')
        for radek in reader:
            kontakty.append(radek)
    return kontakty


def validovat_email(kontakt):
    """email by mel obsahovat: '@' a '.' """
    email = kontakt['email'].strip()
    if email:
        if "@" not in email or "." not in email:
            print(f"Neplatny email nalezen: {email} - opravuji na '-'.")
            kontakt['email'] = "-"
    else:
        print("Neplatny email nalezen: prazdny email - opravuji na '-'.")
        kontakt['email'] = "-"
    return kontakt


def validovat_telefon(kontakt):
    """Projde vsechny telefonni cisla a pokud nejsou validni, nebo chybi data, prepise je na '-' """
    telefon = kontakt['telefon'].strip().replace(' ', '')
    if telefon:
        if telefon.startswith('+420') and len(telefon) == 13:
            return kontakt # telefon je platny, nic nedelame
        elif len(telefon) == 9: # pokud chybi predvolba
            print(f"Opravuji telefon: {kontakt['telefon']}, pridavam predvolbu +420.")
            kontakt['telefon'] = '+420' + telefon
        else: # vsechny ostatni pripady beru za neplatne
            print(f"Neplatny telefon nalezen: {kontakt['telefon']} - opravuji na '-'.")
            kontakt['telefon'] = '-'
    else:
        print("Neplatny telefon nalezen: prazdne telefonni cislo - opravuji na '-'.")
        kontakt['telefon'] = '-'
    return kontakt


def opravit_kontakty(soubor):
    kontakty = nacist_kontakty(soubor)
    for kontakt in kontakty:
        jmeno = str(kontakt["jmeno"]).strip().title()
        prijmeni = str(kontakt["prijmeni"]).strip().title()
        kontakt["jmeno"] = jmeno
        kontakt["prijmeni"] = prijmeni
        if not kontakt["jmeno"].isalpha():
            print(f"Jmeno {kontakt['jmeno']} neni validni, opravuji na '-'")
            kontakt["jmeno"] = "-"
        if not kontakt["prijmeni"].isalpha():
            print(f"Prijmeni {kontakt['prijmeni']} neni validni, opravuji na '-'")
            kontakt["prijmeni"] = "-"
        validovat_telefon(kontakt)
        validovat_email(kontakt)
    return kontakty


x = opravit_kontakty('databanka.csv')
for item in x:
    print(item)
