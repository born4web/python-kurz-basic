from log_file import ErrorLogFile
from load_validate_save import normalizace_radku
from load_validate_save import validace_kontaktu

CONTACT_TABLE_CHARACTER_LENGTH = 40
CONTACT_LABEL_CHARACTER_LENGTH = 10
NAZVY_SLOUPCU = ["Jmeno", "Prijmeni", "Rozliseni", "E-mail", "Telefon"]
log = ErrorLogFile()

def _print_contact_table_row(label: str, value: str): #podtrzitkem rikam, ze to je vyladeny, nesahat
    """
    format tabulky pro prezentaci dat na obrazovku uzivateli (z lekce) pro funkci detail_kontaktu
    """
    #pocet znaku na radku
    len_value = len(value) if value else 0
    #zarovnam label na fixni delku
    formated_label = f"{label:<{CONTACT_LABEL_CHARACTER_LENGTH}}"
    #vypocitat chybejici vypln mezerami pro dany radek
    spaces_needed = CONTACT_TABLE_CHARACTER_LENGTH - len_value - CONTACT_LABEL_CHARACTER_LENGTH - 5 # 3x| + 2x" "
    print(f"| {formated_label}| {value}{" " * spaces_needed} |")

def detail_kontaktu(contact_data: dict, database_id: int):
    """
    vypíše kontakt ze zvalidovane databaze do normalizovanych radku definovanych ve fci _print_contact_table_row
    -------------------------
    | ID: | index v db      |
    -------------------------
    | Jmeno: | Pepa         |
    | Prijmeni: Vomacka     |
    | Rozliseni: ml.        |
    | Email: pepa@seznam.cz |
    | Telefon: 606606606    |
    -------------------------
    """
    _print_contact_table_row("ID", str(database_id))
    print("-"*(1+CONTACT_TABLE_CHARACTER_LENGTH))
    _print_contact_table_row("Jmeno", contact_data.get("Jmeno"))
    _print_contact_table_row("Prijmeni", contact_data.get("Prijmeni"))
    _print_contact_table_row("Rozliseni", contact_data.get("Rozliseni"))
    _print_contact_table_row("E-mail", contact_data.get("E-mail"))
    _print_contact_table_row("Telefon", contact_data.get("Telefon"))
    print("-"*(1+CONTACT_TABLE_CHARACTER_LENGTH))

def smazat_kontakt(database: list):
    """
    smazani kontaktu dle zadaneho cisla / id + kontrola validniho vstupu z klavesnice
    """
    while True:
        try:
            database_id = int(input(f"Zadejte ID kontaktu, ktery chcete odstranit (1 - {len(database)})(nebo 0 pro Zpet): "))
            if database_id == 0:
                break
            smazany_kontakt = database.pop(database_id - 1)
            print("Byl smazan kontakt:")
            detail_kontaktu(smazany_kontakt, database_id)
            log.info_message(f"Uprava databaze uzivatelem - smazani kontaktu ID {database_id} : {smazany_kontakt}")
            break

        except (ValueError, IndexError):
            print(f"Neexistujici kontakt, nebo jste nezadali cislo.")
            continue

def seradit_kontakty(database: list) -> list:
    """
    seradi kontakty v databazi podle prijmeni, pri shode dale dle jmena
    """
    sorted_data = sorted(database, key=lambda x: (x["Prijmeni"], x["Jmeno"]))
    print("Kontakty byly v databazi serazeny dle prijmeni a jmena.")
    log.info_message("Uprava databaze uzivatelem - serazeni kontaktu")
    return sorted_data

def vypsat_kontakt_dle_id(database: list):
    """
    vypise kontakt z databaze dle zadaneho ID kontaktu
    """
    while True:
        try:
            database_id = int(input(f"Zadejte ID kontaktu, ktery chcete zobrazit (1 - {len(database)})(nebo 0 pro Zpet): "))
            if database_id == 0:
                break
            detail_kontaktu(database[database_id-1], database_id)
            break

        except (ValueError, IndexError):
            print(f"Neexistujici kontakt, nebo jste nezadali cislo.")
            continue

def vyhledat_kontakty(database: list):
    """
    vyhledani a vypsani kontaktu odpovidajicim zadanym hodnotam klicu
    """
    hledane_hodnoty = {key: value for key in NAZVY_SLOUPCU if (value := input(f"Zadejte {key} kontaktu (odentrujte, pokud nechcete udaj pouzit k vyhledavani): "))}
    #(hodnota := input(...)) je "walrus operátor" (novinka od Pythonu 3.8), který umožňuje přiřazení hodnoty přímo v podmínce (ChatGPT mi zeefektivnilo for cyklus)

    """
    vyhledavani alespoň jedné shody
    možná modifikace: "all"(misto "any") - vypisi se pouze presne shody
    """
    pocet_nalezenych = 0
    for i, kontakt in enumerate(database):
        if any(hledane_hodnoty[key] == kontakt[key] for key in hledane_hodnoty):
           detail_kontaktu(kontakt, i+1)
           pocet_nalezenych += 1
    print(f"Nebyla nalezena zadna shoda pro:\n{hledane_hodnoty}") if pocet_nalezenych == 0 else print(f"Pro {hledane_hodnoty}\nbylo nalezeno vyhovujicich kontaktů: {pocet_nalezenych}")

def pridat_kontakt(database: list) -> list:
    """
    vytvoreni noveho kontaktu, jeho normalizace, validace, kontrola duplicity a ulozeni do databaze
    """
    novy_kontakt = normalizace_radku({key: value for key in NAZVY_SLOUPCU if (value := input(f"Zadejte {key} kontaktu (odentrujte, pokud nezname): "))})

    if validace_kontaktu(novy_kontakt):
        #kontakt je validni
        zakazane_duplicity = ["Jmeno","Prijmeni","Rozliseni"] #klice jejichz hodnoty se kontrolui, jestli jiz nejsou v databazi
        if duplicita(novy_kontakt, database, zakazane_duplicity):
            print("Kontakt nebyl vytvoren - duplicita")
            log.info_message(f"Novy kontakt nebyl vytvoren - duplicita v klicich {zakazane_duplicity}")

        else:
            print(f"Do databaze byl pridan novy kontakt: {novy_kontakt}")
            database.append(novy_kontakt)
            log.info_message("Uprava databaze uzivatelem - vytvoren novy kontakt")

    else:
        #kontakt neni validni
        print("Kontakt nebyl vytvoren - musi obsahovat (jmeno NEBO prijemni) A (telefon NEBO email)")
        log.info_message("Novy kontakt nebyl vytvoren - nevalidni forma")

    return database

def duplicita(kontakt: dict, database: list, zakazane_duplicity: list) -> bool:
    """
    kontrola duplicity (noveho) kontaktu (kontakt) v existujici databazi (database) na zakladde hodnot vybranych klicu (zakazane_duplictiy)
    """
    for polozka in database:
        if all(kontakt[key] == polozka[key] for key in zakazane_duplicity):
            return True #kontakt je duplictni dle kontrolovanych klicu
    return False