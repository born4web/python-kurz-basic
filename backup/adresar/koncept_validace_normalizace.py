"""
Modul validace a norm,alizace dat kontaktu
{
    'jmeno': '  Pavla  ',
    'prijmeni': 'nováková',
    'rozliseni': '',
    'email': 'pavla@novakopvi.cz',
    'telefon': '987456321',
}
"""
import re
from log_file import ErrorLogFile

# log soubor
log = ErrorLogFile()

# konstanty pro normalizaci
CSV_FIELD_NAME = ['jmeno', 'prijmeni', 'rozliseni', 'email', 'telefon']
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PHONE_PATTERN = re.compile(r'^(\+420)?[0-9]{9}$')


def is_valid_email(email: str) -> bool:
    return EMAIL_PATTERN.match(email) is not None


def is_valid_phone(phone: str) -> bool:
    return PHONE_PATTERN.match(phone) is not None


def normalize_contact_data(contact_data: dict) -> dict:
    """Normalizujeme podobu dat - data jsou na vstupu retezec, pouzijeme jenom pole ktera mame pouzit"""
    contact_data_to_string = {key: str(value) for key, value in contact_data.items() if key in CSV_FIELD_NAME}
    normalizeed_data = {
        'jmeno': contact_data_to_string['jmeno'].strip().capitalize() if contact_data_to_string.get('jmeno') else '',
        'prijmeni': contact_data_to_string['prijmeni'].strip().capitalize() if contact_data_to_string.get('prijmeni') else '',
        'rozliseni': contact_data_to_string['rozliseni'].strip() if contact_data_to_string.get('rozliseni') else '',
        'email': contact_data_to_string['email'].strip() if contact_data_to_string.get('email') else '',
        'telefon': contact_data_to_string['telefon'].strip() if contact_data_to_string.get('telefon') else '',
    }
    return normalizeed_data


def validate_contact_data(contact_data: dict) -> bool:
    """"""
    validation_result = True

    # 1. zda alespon jmeno nebo prijmeni existuje
    if not (contact_data['jmeno'] or contact_data['prijmeni']):
        validation_result = False
        log.error_message(f"Kontakt {contact_data} neobsahuje ani jmeno, ani prijmeni")

    # 2. alespon email nebo telefon musi byt platny
    if not (contact_data['email'] or contact_data['telefon']):
        # oba email i telefon chybeji
        validation_result = False
        log.error_message(f"Kontakt {contact_data} neobsahuje ani email, ani telefon")
    else:
        # 3. email a telefon musi byt platne udaje
        email = contact_data['email']
        if email:
            if not is_valid_email(email):
                validation_result = False
                log.error_message(f"Kontakt {contact_data} neobsahuje platnou emailovou adresu")

        phone = contact_data['telefon']
        if phone:
            if not is_valid_phone(phone):
                validation_result = False
                log.error_message(f"Kontakt {contact_data} neobsahuje platnou telefon")

    # 3. alespon email nebo telefon musi byt platny jiny pristup
    email = contact_data['email']
    if email:
        if not is_valid_email(email):
            email = ""

    phone = contact_data['telefon']
    if phone:
        if not is_valid_phone(phone):
            phone = ""

    if not (email or phone):
        # oba email i telefon chybeji
        validation_result = False
        log.error_message(f"Kontakt {contact_data} neobsahuje ani email, ani telefon")

    return validation_result

