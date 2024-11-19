import csv
import re


class ContactDatabase:
    def __init__(self):
        """
        Inicializuje třídu ContactDatabase a nastaví list na prázdnou hodnotu.
        """
        self.contacts = []

    def getLastIndex(self):
        """
        Najde nejvyšší index v listu kontaktů.
        Returns:
        int: Nejvyšší index zvětšený o jedna
        """
        max_contact = max(self.contacts, key=lambda contact: contact["index"])
        return max_contact["index"] + 1

    def nacist_kontakty_csv(self, fileName):
        """
        Otevře soubor, přečte a rozdělí po řádkách. Z každého řádku vytvoří slovník a přidá atribut index.
        Args:
        fileName (string): Cesta souboru.
        """
        self.contacts = []
        self.fileName = fileName
        try:
            with open(fileName, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                index = 0
                for row in reader:
                    row["index"] = index
                    self.contacts.append(row)
                    index += 1
        except FileNotFoundError:
            print(f"Soubor {fileName} nenalezen, vytvoříme nový.")

    def ulozit_kontakty_csv(self):
        """
        Projde celý list kontaktů a z každého slovníku odebere index. Poté uloží do .csv souboru.
        """
        if not self.contacts:
            print("Žádné kontakty k uložení.")
            return
        contacts_to_save = [
            {k: v for k, v in contact.items() if k != "index"}
            for contact in self.contacts
        ]
        with open(self.fileName, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=contacts_to_save[0].keys())
            writer.writeheader()
            writer.writerows(contacts_to_save)

    def setridit_kontakty(self):
        """
        Setřídí kontakty nejprve podle příjmení, a pokud jsou příjmení shodná, tak podle jména.
        """
        self.contacts.sort(
            key=lambda contact: (contact.get("surname", ""), contact.get("name", ""))
        )

    def vytvorit_kontakt(self, **kwargs):
        """
        Vyberu zadané atributy a vytvořím z nich slovník, který přidám do listu kontaktů.
        Args:
            **kwargs (mixed): Více atributů.
        """
        required_params = ["name", "surname", "phone", "email"]

        if not kwargs.get("name") and not kwargs.get("surname"):
            print("Chyba: Musíte zadat alespoň jméno nebo příjmení.")
            return
        if not kwargs.get("email") and not kwargs.get("phone"):
            print("Chyba: Musíte zadat alespoň email nebo telefon.")
            return
        new_contact = {
            "name": kwargs.get("name"),
            "surname": kwargs.get("surname"),
            "email": kwargs.get("email"),
            "phone": kwargs.get("phone"),
            "difference": kwargs.get("difference", ""),
            "index": self.getLastIndex(),
        }

        for contact in self.contacts:
            if (
                contact["name"] == new_contact["name"]
                and contact["surname"] == new_contact["surname"]
                and contact["difference"] == new_contact["difference"]
            ):
                print("Tento kontakt již existuje, duplicitní záznam není povolen.")
                return

        self.contacts.append(new_contact)
        print(
            f"Kontakt {new_contact['name']} {new_contact['surname']} byl úspěšně přidán."
        )

    def smazat_kontakt(self, index=None, name=None, surname=None, difference=""):
        """
        Smaže kontakt na základě zadání jména, příjmení a indexu.
        Args:
            index (int): Index kontaktu.
            name (string): Jméno kontaktu.
            surname (string): Příjmení kontaktu.
            difference (string): Rozlišení kontaktu.
        Returns:
            None: Pro ukončení funkce.
        """
        if index != None:
            tmp_index = None
            found = False
            for key, cont in enumerate(self.contacts):
                if cont["index"] == index:
                    found = True
                    self.contacts.pop(index)
            if not found:
                print(f"Chyba: Kontakt s indexem {index} neexistuje.")
                return
            print(f"Kontakt byl úspěšně smazán.")
            return

        if name and surname:
            for i, contact in enumerate(self.contacts):
                if (
                    contact["name"] == name
                    and contact["surname"] == surname
                    and contact["difference"] == difference
                ):
                    deleted_contact = self.contacts.pop(i)
                    print(
                        f"Kontakt {deleted_contact['name']} {deleted_contact['surname']} byl úspěšně smazán."
                    )
                    return
            print(
                f"Chyba: Kontakt {name} {surname} s rozlišením '{difference}' nebyl nalezen."
            )
        else:
            print(
                "Chyba: Musíte zadat buď index kontaktu, nebo kombinaci jméno, příjmení a rozlišení."
            )

    def najit_kontakt(self, **kwargs):
        """
        Vyhledá kontakt podle zadaných parametrů.
        Args:
            **kwargs (mixed): Více atributů.
        Returns:
            list: List nalezených kontaktů.
        """
        search_criteria = {key: value for key, value in kwargs.items() if value}
        if not search_criteria:
            print("Chyba: Musíte zadat alespoň jedno kritérium pro hledání.")
            return []

        found_contacts = []
        for contact in self.contacts:
            match = True
            for key, value in search_criteria.items():
                if contact.get(key) != value:
                    match = False
                    break
            if match:
                found_contacts.append(contact)

        if found_contacts:
            print(f"Nalezeno {len(found_contacts)} kontakt(ů):")
            for contact in found_contacts:
                self.detail_kontaktu(contact)
        else:
            print("Žádné kontakty nebyly nalezeny.")
        return found_contacts

    def detail_kontaktu(self, contact):
        """
        Vypíše detail kontaktu do formátované tabulky.
        Args:
            contact (dictionary): Jeden určitý kontakt.
        """
        column_width = 20
        print("-" * (column_width + 2 + 30))
        print(f"| {'Jméno:':<{column_width}} | {contact.get('name', ''):<30} |")
        print(f"| {'Příjmení:':<{column_width}} | {contact.get('surname', ''):<30} |")
        difference = contact.get("difference", "")
        if difference:
            print(f"| {'Rozlišení:':<{column_width}} | {difference:<30} |")
        else:
            print(f"| {'Rozlišení:':<{column_width}} | {' ':<30} |")
        print(f"| {'Telefon:':<{column_width}} | {contact.get('phone', ''):<30} |")
        print(f"| {'Email:':<{column_width}} | {contact.get('email', ''):<30} |")
        print(f"| {'Index:':<{column_width}} | {contact.get('index', ''):<30} |")
        print("-" * (column_width + 2 + 30))

    def vypsat_kontakty(self):
        """
        Postupně vypíše všechny kontakty.
        """
        for contact in self.contacts:
            invalid_name = re.search("[0-9]", contact["name"])
            invalid_surname = re.search("[0-9]", contact["surname"])
            valid_phone = re.search(r"^(\+420)?[0-9]{9}$", contact["phone"])
            vaild_email = re.search(
                r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$", contact["email"]
            )
            if invalid_name or invalid_surname or not valid_phone or not vaild_email:
                continue
            self.detail_kontaktu(contact)


# Příklad použití
def main_menu():
    """
    Vypíše možnosti hlavního menu. Poté se podle zadaného čísla provede určítá operace v match case.
    """
    while True:
        print("\nHlavní menu:")
        print("1. Zobrazit všechny kontakty")
        print("2. Přidat nový kontakt")
        print("3. Upravit kontakt")
        print("4. Odstranit kontakt")
        print("5. Zobrazit detail kontaktu")
        print("6. Najít kontakt")
        print("7. Setřídit kontakt")
        print("8. Uložit a ukončit")
        print("9. Ukončit bez uložení")

        try:
            choice = int(input("Zadejte číslo akce: "))
        except ValueError:
            print("\nNeplatná volba!")
            continue
        if choice < 1 or choice > 9:
            print("\nZvolte číslo akce mezi 1 a 9.")
            continue
        match choice:
            case 1:
                contact.vypsat_kontakty()
            case 2:
                name = input("Zadejte jméno: ")
                surname = input("Zadejte příjmení: ")
                phone = input("Zadejte telefon: ")
                email = input("Zadejte email: ")
                difference = input("Zadejte rozlišení (nepovinné): ")
                contact.vytvorit_kontakt(
                    name=name,
                    surname=surname,
                    phone=phone,
                    email=email,
                    difference=difference,
                )
            case 3:
                name = input("Zadejte jméno kontaktu k úpravě: ")
                surname = input("Zadejte příjmení kontaktu k úpravě: ")
                found_contacts = contact.najit_kontakt(name=name, surname=surname)
                if found_contacts:
                    index = int(input("Zadejte index kontaktu k úpravě: "))
                    tmp_cont = None
                    for cont in found_contacts:
                        if cont["index"] == index:
                            tmp_cont = cont

                    if tmp_cont != None:
                        updated_name = (
                            input("Nové jméno (nechte prázdné pro zachování): ")
                            or tmp_cont["name"]
                        )
                        updated_surname = (
                            input("Nové příjmení (nechte prázdné pro zachování): ")
                            or tmp_cont["surname"]
                        )
                        updated_phone = (
                            input("Nový telefon (nechte prázdné pro zachování): ")
                            or tmp_cont["phone"]
                        )
                        updated_email = (
                            input("Nový email (nechte prázdné pro zachování): ")
                            or tmp_cont["email"]
                        )
                        updated_difference = (
                            input("Nové rozlišení (nechte prázdné pro zachování): ")
                            or tmp_cont["difference"]
                        )

                        contact.smazat_kontakt(index=index)
                        contact.vytvorit_kontakt(
                            name=updated_name,
                            surname=updated_surname,
                            phone=updated_phone,
                            email=updated_email,
                            difference=updated_difference,
                        )
                    else:
                        print("Neplatný index.")
            case 4:
                name = input("Zadejte jméno kontaktu k odstranění: ")
                surname = input("Zadejte příjmení kontaktu k odstranění: ")
                difference = input("Zadejte rozlišení kontaktu k odstranění: ")
                contact.smazat_kontakt(
                    name=name, surname=surname, difference=difference
                )
            case 5:
                index = int(input("Zadejte index kontaktu pro zobrazení detailu: "))
                found = False
                for cont in contact.contacts:
                    if cont["index"] == index:
                        found = True
                        contact.detail_kontaktu(cont)
                if not found:
                    print("Neplatný index.")
            case 6:
                name = input("Zadejte jméno k vyhledání: ")
                surname = input("Zadejte příjmení k vyhledání: ")
                contact.najit_kontakt(name=name, surname=surname)
            case 7:
                contact.setridit_kontakty()
                print("Kontakty byly setříděny.")
            case 8:
                contact.ulozit_kontakty_csv()
                print("Kontakty byly uloženy. Ukončení programu.")
                return
            case 9:
                return


if __name__ == "__main__":
    contact = ContactDatabase()
    FILENAME = "contacts.csv"
    contact.nacist_kontakty_csv(FILENAME)
    main_menu()
