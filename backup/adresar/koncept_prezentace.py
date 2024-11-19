"""Prezentace dat na obrazovku uzivateli

-----------------
| ID: | index v db |
-----------------
| Jmeno: | Pepa |
-----------------

"""

CONTACT_TABLE_CHARACTER_LENGTH = 40
CONTACT_LABEL_CHARACTER_LENGTH = 10


def _print_contact_table_row(label: str, value: str):
    # Delka hodnoty
    len_value = len(value) if value else 0
    # zarovname label na fixni delku
    formatted_label = f"{label:<{CONTACT_LABEL_CHARACTER_LENGTH}}"
    # vypocitat chybejici vypln mezerami pro dany radek
    #  '|' + ' ' + '|' + ' ' + '|'
    spaces_needed = CONTACT_TABLE_CHARACTER_LENGTH - CONTACT_LABEL_CHARACTER_LENGTH - len_value - 5
    print(f"| {formatted_label}| {value}{' ' * spaces_needed}|")


def detail_kontaktu(contact_data: dict, database_id: int = None):
    """"""
    if contact_data:
        print("-" * CONTACT_TABLE_CHARACTER_LENGTH)
        if database_id is not None:
            _print_contact_table_row("ID", str(database_id))
            print("-" * CONTACT_TABLE_CHARACTER_LENGTH)
        _print_contact_table_row("Jmeno", contact_data.get('jmeno'))
        _print_contact_table_row("Prijmeni", contact_data.get('prijmeni'))
        _print_contact_table_row("Rozliseni", contact_data.get('rozliseni'))
        _print_contact_table_row("Email", contact_data.get('email'))
        _print_contact_table_row("Telefon", contact_data.get('telefon'))
        print("-" * CONTACT_TABLE_CHARACTER_LENGTH)


if __name__ == "__main__":
    data = {'jmeno': 'jan', 'prijmeni': 'Hulák', 'rozliseni': '', 'email': 'jan@hulakovi.cz', 'telefon': '159753654'}
    detail_kontaktu(data)
