"""
Vlastni "aplikace" pro spravu kontaktu
"""
from log_file import ErrorLogFile
from koncept_soubory import *
from koncept_prezentace import *
from koncept_validace_normalizace import *


def force_keyboard_input():
    """"""
    i = 0
    while True:
        i += 1
        if i == 10:
            print("BREAK")
        else:
            print('ve ok')
        try:
            # vstup z klavesnice
            x = input("Zadej slovo: ")
            # validace vstupu
            if not x.isalpha():
                print("Slovo musi obsahovat pouze pismena")
                continue
            else:
                if x == "q":
                    print("Konec programu")
                    return "Nebylo nic zadano"
                return x
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass


def vypsat_kontakty(database: list):
    """"""
    for index, polozka in enumerate(database):
        detail_kontaktu(polozka, index)


def smazat_kontakt(database: list, database_id: int):
    """"""
    if database:
        try:
            return database.pop(database_id)
        except IndexError:
            print("Neexistujici kontakt")


def setridit_kontakty(database: []):
    """"""
    sorted_data = sorted(database, key=lambda x: (x['prijmeni'], x['jmeno']))
    return sorted_data


def porovnej_shodu_vsech_parametru(database_item: dict, **kwargs):
    """
    database_itemn - kontakt z databaze
    **kwargs - testovane, hledane parametry kontaktu
    """
    for key, value in kwargs.items():
        if key not in database_item.keys():
            return False
        else:
            if database_item[key] != str(value):
                return False
    return True


def najit_kontakt(database: dict, **kwargs):
    """"""
    result = [(index, polozka) for index, polozka in enumerate(database) if porovnej_shodu_vsech_parametru(polozka, **kwargs)]
    return result


def otestuj_duplicitni_kontakt(database: dict, **kwargs):
    """"""
    testovane_parametry = ['jmeno', 'prijmeni', 'rozliseni']
    hledane_parametry = {key: value for key, value in kwargs.items() if key in testovane_parametry}

    return najit_kontakt(database, **hledane_parametry)


def upravit_kontakt(database: [], database_id: int, **kwargs):
    """Delete contact at index position"""
    normalized_data = normalize_contact_data(kwargs)
    validated_data = validate_contact_data(normalized_data)
    if not validated_data:
        print("Neplatná data")
    else:
        try:
            database[database_id].update(normalized_data)
        except IndexError:
            print(f"Neexistujici kontakt s ID: {database_id}")


# nalezene_kontakty = najit_kontakt(**kwargs)
# for kontakt_s_indexem in nalezene_kontakty:
#     print("mazu kontakt")
#     detail_kontaktu(kontakt_s_indexem[1])
#     smazat_kontakt(database, kontakt_s_indexem[0])


databanka = nacist_kontakty_csv()
vypsat_kontakty(databanka)

