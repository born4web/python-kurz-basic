# Funkce pro nalezení kontaktu
def najit_kontakt(**kwargs):
    """Vyhledá kontakt podle zadaných parametrů (jméno, příjmení, rozlišení, email, telefon)."""
    # Normalizace vstupních dat
    normalized_data = normalize_contact_data(kwargs)

    nalezene_kontakty = []
    for contact in kontakty:
        match = True
        for key, value in normalized_data.items():
            if key in contact and value and value != contact[key]:
                match = False
                break
        if match:
            nalezene_kontakty.append(contact)
    if nalezene_kontakty:
        for kontakt in nalezene_kontakty:
            detail_kontaktu(kontakt)
        log.info_message(f'Nalezeny kontakty: {nalezene_kontakty}')
        return nalezene_kontakty
    else:
        log.error_message('Žádné kontakty nebyly nalezeny podle zadaných kritérií.')
        return None