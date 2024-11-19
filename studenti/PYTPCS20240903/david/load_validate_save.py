"""
modul s funkcemi pro import/export datbaze ze/do souboru:
- nacteni databaze ze souboru .csv
- normalizace dat
- validace dat // validni kontakt = obsahuje (jmeno NEBO prijemni) A (telefon NEBO email)
- odstraneni duplicitnich zaznamu v nactene databazi
- ulozeni databaze do souboru .csv
"""

import csv
import re
from fileinput import close
from log_file import ErrorLogFile

#konstanty pro normalizaci
NAZVY_SLOUPCU = ["Jmeno", "Prijmeni", "Rozliseni", "E-mail", "Telefon"]
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PHONE_PATTERN = re.compile(r'^(\+420)?[0-9]{9}$')
log = ErrorLogFile()

def nacist_kontakty_csv(file: str = "databanka.csv", sloupce: list = NAZVY_SLOUPCU, oddelovac = ",") -> list:
    """
    funkce pro nacteni databaze z csv soubrou 'databanka.csv', ktery pouziva jako oddelovac sloupcu ','
    postupne normalizuje a validuje nacitane radky - do databaze se pridavaji pouze platne kontakty, dale probehen odstraneni duplicitnich kontaktu
    vraci seznam(:list) vizitek(:dict)
    """

    with open(file, "r", encoding="utf-8") as soubor:
        reader = csv.DictReader(soubor, delimiter=oddelovac, fieldnames=sloupce)
        seznam_vizitek = []  # promenna typu list pro zvalidovane / platne vizitky
        i = 1

        for radek_csv in reader:
            radek_csv = normalizace_radku(radek_csv)
            seznam_vizitek.append(radek_csv) if validace_kontaktu(radek_csv) else log.error_message(f"{i}. kontakt neni platny") #pokud kontakt neni validni, vypise do logfile cislo radku
            i += 1

    log.info_message(f"Nacteni souboru {file} do databaze")

    bez_duplicit = odstraneni_duplicit(seznam_vizitek)

    pocet_duplicit = len(seznam_vizitek) - len(bez_duplicit)
    if pocet_duplicit > 0:
        print(f"Z nacteneho souboru {file} byly odstraneny duplicitni kontakty ({pocet_duplicit}).")
        log.warning_message(f"Odstraneny duplicitni kontakty ({pocet_duplicit}).")

    print("Soubor databanka.scv byl nacten a zvalidovan. Co dal?")
    seznam_vizitek.clear()

    return bez_duplicit

def normalizace_radku(radek_csv: dict) -> dict:
    #prevedeni values slovniku na retezec, odstraneni prazdnych znaku
    to_string = {key: str(value).strip() for key, value in radek_csv.items() if key in NAZVY_SLOUPCU}

    normalized_data = {
        "Jmeno": to_string["Jmeno"].strip().capitalize() if to_string.get("Jmeno") else "",
        "Prijmeni": to_string["Prijmeni"].strip().capitalize() if to_string.get("Prijmeni") else "",
        "Rozliseni": to_string["Rozliseni"].strip() if to_string.get("Rozliseni") else "",
        "E-mail": to_string["E-mail"].strip() if to_string.get("E-mail") else "",
        "Telefon": to_string["Telefon"].strip() if to_string.get("Telefon") else "",
    }
    return normalized_data

def odstraneni_duplicit(database: list, **kwargs) -> list:
    """
    Odstraní duplicity na základě všech klíčů, případně kwargs umožní určit, které klíče poslouží pro identifikaci duplicit
    porovnava hodnoty/kontakty v nactene databazi vzajemne - v modulu funkce_databaze mam vyhledani duplicity kontaktu(dict) v databazi
    zde mam tuto formu zduvodu kontroly vstupniho souboru - informace kolik je ve vstupnim souboru stejnych radku je uzitecna - odhali pripadny problem pri tvorbe souboru (ackoliv ten kdo vytvari vstupni soubor by snad sam mal zajistit, aby byl bez duplicit)
    """
    databaze_bez_duplicit = []
    obsahuje = set()  #set pro uložení unikátní kombinace polí

    #poradilo chatgpt...
    for kontakt in database:
        # pokud jsou kwargs prázdné, použije se celý kontakt jako klíč
        if not kwargs:
            key = tuple(kontakt.items())  #všechny klíče a jejich hodnoty
        else:
            #pouze hodnoty vybranych klíčů
            key = tuple(kontakt[value] for value in kwargs.values() if value in kontakt)

        if key not in obsahuje:
            obsahuje.add(key)
            databaze_bez_duplicit.append(kontakt)

    return databaze_bez_duplicit

def validace_kontaktu(kontakt: dict) -> bool:
    validation_result = True

    # funkce pro kontrolu formatu emailu a telefonniho cisla:
    def is_valid_email(email: str) -> bool:
        return EMAIL_PATTERN.match(email) is not None

    def is_valid_phone(phone: str) -> bool:
        return PHONE_PATTERN.match(phone) is not None

    # Existuje jmeno nebo prijmeni?
    if not (kontakt["Jmeno"] or kontakt["Prijmeni"]):
        validation_result = False
        log.warning_message(f"Kontakt {kontakt} musi mit zadane alespon jmeno nebo prijmeni")

    email = kontakt["E-mail"]
    phone = kontakt["Telefon"]

    if email:
        if not is_valid_email(email):
            email = ""
    if phone:
        if not is_valid_phone(phone):
            phone = ""

    # Existuje po validaci email nebo telefon?
    if not (email or phone):
        validation_result = False
        log.warning_message(f"Kontakt {kontakt} neobsahuje ani platny email ani platny telefon")

    return validation_result

def ulozit_kontakty_csv(database: [], file: str = "databanka1.csv", oddelovac = ",") -> list:
    """
    funkce pro ulozeni do jineho csv souboru
    """

    welcome_message = "Ukladam data..."
    closing_message = "...ulozeno do souboru"

    print(welcome_message)

    with open(file, "w", encoding="utf-8") as soubor:
        writer = csv.DictWriter(soubor, delimiter=oddelovac, fieldnames=NAZVY_SLOUPCU)

        writer.writeheader()
        writer.writerows(database)

    print(f"{closing_message} {file}")
    log.info_message(f"{closing_message} {file}")