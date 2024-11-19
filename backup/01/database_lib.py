"""
Modul obsluznych funkci pro praci s daty z CSV databaze
"""
import csv
from src.knihovny.validace import normalizuj_contact_data, validate_contact_data
from src.knihovny.constanty import *


def nacist_kontakty_csv(file_path="databanka.csv", delimiter=',', quotechar='"'):
    """Nacte data z CSV souboru a vrati mi je jako seznam - list"""
    print("------------ Nacitam data do databaze kontaktu ------------")
    with open(file_path, "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter, quotechar=quotechar)
        database = []
        for item in reader:
            normalized_data = normalizuj_contact_data(item)
            if validate_contact_data(normalized_data):
                database.append(normalized_data)
    print("---------------------- Data nactena -----------------------")
    return database


def ulozit_kontakty_csv(database, file_path="databanka_new.csv", delimiter=',', quotechar='"'):
    """"""
    print("------------ Ukladam data do databaze kontaktu ------------")
    with open(file_path, "w", encoding='utf-8', newline="") as csvfile:
        writer = csv.DictWriter(csvfile,
                                delimiter=delimiter,
                                quotechar=quotechar,
                                fieldnames=CSV_FIELD_NAMES)
        writer.writeheader()
        writer.writerows(database)
    print("---------------------- Data ulozena -----------------------")


def _print_contact_table_row(label: str, value: str):
    """"""
    len_value = len(value) if value else 0
    formatted_label = f"{label:<{CONTACT_LABEL_CHARACTER_LENGTH}}"
    space_needed = CONTACT_TABLE_CHARACTER_LENGTH - CONTACT_LABEL_CHARACTER_LENGTH - len_value - 5  # "|" + " " + "|" + " " + "|"
    print(f"| {formatted_label}| {value}{' '*space_needed}|")


def detail_kontaktu(contact_data, database_id=None):
    """Formatovany vystup jednoho zaznamu na obrazovku, popripade i s indexem v databazi...
    ---------------------------
    | ID:       | 123
    ---------------------------
    | Jmeno:    | Jan
    | Prijmeni: | Novak
    |Rozliseni: | ml.
    | Telefon:  | +420603603603
    |Email:     | jan@novakovi.cz
    ---------------------------
    """
    if contact_data:
        print("-"*CONTACT_TABLE_CHARACTER_LENGTH)
        if database_id is not None:
            _print_contact_table_row("ID", str(database_id))
            print("-"*CONTACT_TABLE_CHARACTER_LENGTH)
        _print_contact_table_row('Jmeno', contact_data['jmeno'])
        _print_contact_table_row('Prijmeni', contact_data['prijmeni'])
        _print_contact_table_row('Rozliseni', contact_data['rozliseni'])
        _print_contact_table_row('Telefon', contact_data['telefon'])
        _print_contact_table_row('Email', contact_data['email'])
        print("-"*CONTACT_TABLE_CHARACTER_LENGTH)


def smazat_kontakt(contact_data, database_id):
    """"""
    if contact_data:
        try:
            return contact_data.pop(database_id)
        except IndexError:
            print(f"Neexistujici kontakt s ID: {database_id}")
    return False


def vypsat_kontakty(database: []):
    """"""
    print("---------- VYPIS VSECH KONTAKTU ----------")
    for index, contact in enumerate(database):
        detail_kontaktu(contact, index)
    print("------------------------------------------")


def porovnej_shodu_vsech_parametru(contact_data, **kwargs):
    """Porovname contact data s kwargs hledanymi parametry

    :return: True/False - vsechny se shoduji / ne vsechny se shoduji
    """
    for key, value in kwargs.items():
        if key not in contact_data:
            return False
        else:
            if contact_data[key] != str(value):
                return False
    return True


def najit_kontakt(databaze, **kwargs):
    """Vyhleda podle predanych kriterii vsechny kontakty ktere kriteriim vyhovuji"""
    result = [(index, contact) for index, contact in enumerate(databaze) if porovnej_shodu_vsech_parametru(contact, **kwargs)]
    return result


def setridit_kontakty(databaze):
    """Setridime kontakty podle Prijmeni a nasledne idealne podle Jmena"""
    sorted_data = sorted(databaze, key=lambda x: (x['prijmeni'], x['jmeno']))
    return sorted_data


def _otestuj_duplicitni_kontakt(database, **kwargs):
    """"""
    testovane_parametry = ['jmeno', 'prijmeni', 'rozliseni']
    redukovany_kontakt = {key: value for key, value in kwargs.items() if key in testovane_parametry}
    #redukovany_kontakt = {key: kwargs[key] for key in testovane_parametry if key in kwargs}

    return najit_kontakt(database, **redukovany_kontakt)


def vytvorit_kontakt(database, **kwargs):
    """"""
    normalized_data = normalizuj_contact_data(kwargs)
    validated_data = validate_contact_data(normalized_data)
    if validated_data:
        duplicita = _otestuj_duplicitni_kontakt(database, **normalized_data)
        if not duplicita:
            database.append(normalized_data)
        else:
            print(f"Zadany kontakt jiz v databazi existuje: {duplicita}")


def prepsat_kontakt(database, database_id, **kwargs):
    """Prepise existujici kontakt zcela novymi daty"""
    normalized_data = normalizuj_contact_data(kwargs)
    validated_data = validate_contact_data(normalized_data)
    if validated_data:
        if not _otestuj_duplicitni_kontakt(database, **normalized_data):
            database[database_id].update(normalized_data)
        else:
            print(f"Zmeny ktere jste zadali vedou k duplicite kontaktu: {kwargs}")


def update_kontakt(database, database_id, **kwargs):
    """"""
    try:
        existujici_kontakt = database[database_id]
        existujici_kontakt.update(kwargs)
        prepsat_kontakt(database, database_id, **existujici_kontakt)
    except KeyError:
        print("Kontakt neexistuje")


if __name__ == "__main__":
    # nacti data z databaze
    databaze = nacist_kontakty_csv()
    # smazat_kontakt(databaze, 0)
    test_data = {
        'jmeno': 'homer',
        'email': 'homer@simpsons.com',
    }
    hledana_data = {
        'jmeno': 'Jan',
        'prijmeni': 'Novák',
    }
    prepsat_data = {
        'jmeno': 'homer',
        'prijmeni': 'simpson',
        'email': 'homer@simpsons.com',
    }
    update_data = {
        'rozliseni': 'st.',
    }
    vytvorit_kontakt(databaze, **test_data)
    databaze = setridit_kontakty(databaze)
    vypsat_kontakty(databaze)
    update_kontakt(databaze, 7, **update_data)
    vypsat_kontakty(databaze)

