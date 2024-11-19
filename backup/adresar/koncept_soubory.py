"""
Modul kde demonstrujeme praci se soubory v ramci zaverecneho projektu
"""
import csv
from log_file import ErrorLogFile

# log soubor
log = ErrorLogFile()

CSV_FIELD_NAME = ['jmeno', 'prijmeni', 'rozliseni', 'email', 'telefon']


def nacist_kontakty_csv(file_path: str = "databanka.csv", delimiter: str = ",") -> list:
    """"""
    welcome_message = "Nacitam data do databaze kontaktu ze souboru"
    closing_message = "Data nactena"
    print(f"---------- {welcome_message} ----------")
    log.info_message(welcome_message)

    with open(file_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        database = []
        for radek in reader:
            # 1. normalizuj data
            # 2. validuj data
            database.append(radek)

    print(f"---------- {closing_message} ----------")
    log.info_message(closing_message)
    return database


def ulozit_kontakty_csv(database: [], file_path: str = "databanka1.csv", delimiter: str = ",") -> list:
    """"""
    welcome_message = "Ukladam data z databaze kontaktu do souboru"
    closing_message = "Data ulozena"
    print(f"---------- {welcome_message} ----------")
    log.info_message(welcome_message)

    with open(file_path, "w", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file,
                                delimiter=delimiter,
                                fieldnames=CSV_FIELD_NAME)
        writer.writeheader()
        writer.writerows(database)

    print(f"---------- {closing_message} ----------")
    log.info_message(closing_message)


if __name__ == "__main__":
    kontakty = nacist_kontakty_csv()
    for item in kontakty:
        print(item)
    ulozit_kontakty_csv(kontakty)
