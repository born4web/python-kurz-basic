"""
**********************
|        MENU        |
| ukoncit program:  0|
| nacist soubor:    1|
| vypsat kontakty:  2|
| smazat kontakt:   3|
| seradit databazi: 4|
| vypsat kontakt:   5|
| vyhledat kontakty:6|
| pridat kontakt:   7|
| ulozit databazi:  8|
| napoveda:         9|
**********************
vypise menu a dle vstupu z klavesnice povola patricnou funkci z prislusneho modulu
"""


from log_file import ErrorLogFile

from load_validate_save import nacist_kontakty_csv  #1
from load_validate_save import ulozit_kontakty_csv  #8

from funkce_databaze import detail_kontaktu         #2
from funkce_databaze import smazat_kontakt          #3
from funkce_databaze import seradit_kontakty        #4
from funkce_databaze import vypsat_kontakt_dle_id   #5
from funkce_databaze import vyhledat_kontakty       #6
from funkce_databaze import pridat_kontakt          #7


MENU_TABLE_CHARACTER_LENGTH = 23
MENU_LABLE_CHARACTER_LENGTH = 17
MENU = "MENU"
POLOZKY_MENU = ["ukoncit program","nacist soubor", "vypsat kontakty", "smazat kontakt", "seradit databazi", "vypsat kontakt", "najit kontakty",
                "pridat kontakt", "ulozit databazi", "napoveda", ]
log = ErrorLogFile()


def _menu():
    "funkce pro vypsani nabidky a cisel voleb"

    print("*"*MENU_TABLE_CHARACTER_LENGTH)
    print(f"|{MENU:^{MENU_TABLE_CHARACTER_LENGTH-2}}|")
    for i, polozka in enumerate(POLOZKY_MENU):
        print(f"| {polozka:<{MENU_LABLE_CHARACTER_LENGTH}}: {i}|")
    print("*"*MENU_TABLE_CHARACTER_LENGTH)

def vstup_klavesnice():
    """
    funkce nacita vstup z klavesnice, kontroluje zda je ve spravnem formatu (cele cislo v rozmezi 1 - pocet polozek nabidky)
    vyvolava zvolenou funkci
    """
    while True:
        try:
            vstup = int(input("Zadejte cislo akce (9 = napoveda, 0 = ukonceni programu): "))

            if vstup not in range(0, len(POLOZKY_MENU)):
                print(f"Zadejte CELE CISLO od 0 do {len(POLOZKY_MENU)-1}")
                continue

            #zpracovani validniho vstupu z klavesnice
            match vstup:

                case 0:
                    print("Konec programu")
                    log.info_message("Ukonceni programu")
                    break

                case 1:
                    databanka = nacist_kontakty_csv()
                    print(f"Pocet validnich unikatnich kontaktu = {len(databanka)}")
                    continue

                case 2:
                    for id_kontaktu, item in enumerate(databanka, start=1):
                        detail_kontaktu(item, id_kontaktu)
                    continue

                case 3:
                    smazat_kontakt(databanka)
                    print(f"pocet zbyvajicich kontaktu = {len(databanka)}")
                    continue

                case 4:
                    databanka = seradit_kontakty(databanka)
                    continue

                case 5:
                    vypsat_kontakt_dle_id(databanka)
                    continue

                case 6:
                    vyhledat_kontakty(databanka)
                    continue

                case 7:
                    databanka = pridat_kontakt(databanka)
                    print(f"Pocet validnich unikatnich kontaktu = {len(databanka)}")
                    continue

                case 8:
                    ulozit_kontakty_csv(databanka)
                    continue

                case 9:
                    _menu()
                    continue

        #zachytavani vyjimek
        except ValueError:
            print(f"Zadejte CELE CISLO od 1 do {len(POLOZKY_MENU)-1}")
        except UnboundLocalError:
            print("Databanka je prazdna, nejdrive nactete soubor (volba 1)")
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass

#prvotni vypsani menu a spustění funkce pro zpracovani vstupu z klavesnice (= "spusteni programu")
_menu()
log.info_message("Spusteni programu")
vstup_klavesnice()

