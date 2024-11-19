import csv

# Načítání kontaktů ze souboru CSV
def load_contacts(filename):
    contacts = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print(f"Soubor {filename} nenalezen, vytvoříme nový.")
    print(contacts)
    return contacts

# Uložení kontaktů do CSV
def save_contacts(filename, contacts):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['name', 'phone', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

# Zobrazení všech kontaktů
def show_contacts(contacts):
    if not contacts:
        print("Adresář je prázdný.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Jméno: {contact['name']}, Telefon: {contact['phone']}, Email: {contact['email']}")

# Přidání nového kontaktu
def add_contact(contacts):
    name = input("Zadejte jméno: ")
    phone = input("Zadejte telefon: ")
    email = input("Zadejte email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print("Kontakt byl přidán.")

# Úprava kontaktu
def edit_contact(contacts):
    show_contacts(contacts)
    try:
        index = int(input("Zadejte číslo kontaktu k úpravě: ")) - 1
        if 0 <= index < len(contacts):
            name = input(f"Zadejte nové jméno (aktuálně {contacts[index]['name']}): ") or contacts[index]['name']
            phone = input(f"Zadejte nový telefon (aktuálně {contacts[index]['phone']}): ") or contacts[index]['phone']
            email = input(f"Zadejte nový email (aktuálně {contacts[index]['email']}): ") or contacts[index]['email']
            contacts[index] = {'name': name, 'phone': phone, 'email': email}
            print("Kontakt byl upraven.")
        else:
            print("Neplatné číslo kontaktu.")
    except ValueError:
        print("Neplatný vstup.")

# Odstranění kontaktu
def delete_contact(contacts):
    show_contacts(contacts)
    try:
        index = int(input("Zadejte číslo kontaktu k odstranění: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            print("Kontakt byl odstraněn.")
        else:
            print("Neplatné číslo kontaktu.")
    except ValueError:
        print("Neplatný vstup.")

# Hlavní menu
def main_menu(filename):
    contacts = load_contacts(filename)
    print(contacts)

    while True:
        print("\nHlavní menu:")
        print("1. Zobrazit všechny kontakty")
        print("2. Přidat nový kontakt")
        print("3. Upravit kontakt")
        print("4. Odstranit kontakt")
        print("5. Uložit a ukončit")

        choice = input("Vyberte akci: ")

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(filename, contacts)
            print("Kontakty byly uloženy. Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

# Spuštění programu
if __name__ == "__main__":
    FILENAME = 'contacts.csv'
    main_menu(FILENAME)
