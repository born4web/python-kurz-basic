import csv
import re
import datetime

from log_file import ErrorLogFile
from pathlib import Path

DATA_SLOUPCE = ["jmeno", "prijmeni", "rozliseni", "email", "telefon"]
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
PHONE_PATTERN = re.compile(r'^(\+420)?[0-9]{9}$')
SIRKA_SLOUPCE_1 = 52
SIRKA_SLOUPCE_2 = 15


class Databaze:
    """Trida slouzi pro spravu a manipulaci s kontakty z CSV souboru."""

    def __init__(self, log: ErrorLogFile, soubor: str = None):
        """
        Inicializuje instanci tridy Databaze.
         Args:
            log (ErrorLogFile): Instance tridy pro logovani chyb.
            soubor (str, optional): Cesta k CSV souboru. Vychozi hodnota je None.
        """
        self.kontakty = []
        self.log = log
        self.soubor = None
        if soubor:
            self.cesta_soubor(soubor)

    def __str__(self):
        """
        Vraci prehlednou textovou reprezentaci objektu Databaze.
        Returns:
            str: Informace o poctu kontaktu v databazi.
        """
        return f"Databaze s {len(self.kontakty)} kontakty"

    def __repr__(self):
        """
        Vraci oficialni reprezentaci objektu Databaze.
        Returns:
            str: Retezec, ktery obsahuje nazev souboru a seznam kontaktu.
        """
        return f"Databaze(soubor = {self.soubor}, kontakty= {self.kontakty}"

    def cesta_soubor(self, soubor: str):
        """
        Nastavi cestu k souboru a provede validaci.
        Args:
            soubor (str): Cesta k CSV souboru.
        Raises:
            FileNotFoundError: Pokud soubor neexistuje.
        """
        path = Path(soubor)
        if path.exists() and path.is_file():
            self.soubor = path
            self.log.info_message(f"Cesta k souboru {soubor} byla nastavena.")
        else:
            self.log.error_message(f"Soubor '{soubor}' nebyl nalezen!")
            raise FileNotFoundError(f"Soubor '{soubor}' nebyl nalezen.")

    def normalizace_dat(self, kontakt: dict) -> dict:
        """
        Normalizuje data kontaktu do spravne podoby pro dalsi praci.
        Args:
            kontakt (dict): Kontakt ve forme slovniku.
        Returns:
            dict: Normalizovana data kontaktu.
        """
        data_na_string = {klic: str(hodnota) for klic, hodnota in kontakt.items() if klic in DATA_SLOUPCE}
        normalizovana_data = {
            'jmeno':     data_na_string['jmeno'].strip().title() if data_na_string.get('jmeno') else '',
            'prijmeni':  data_na_string['prijmeni'].strip().title() if data_na_string.get(
                'prijmeni') else '',
            'rozliseni': data_na_string['rozliseni'].strip().lower() if data_na_string.get(
                'rozliseni') else '',
            'email':     data_na_string['email'].strip().lower() if data_na_string.get('email') else '',
            'telefon':   data_na_string['telefon'].strip().replace(' ', '') if data_na_string.get(
                'telefon') else ''
        }
        return normalizovana_data

    def validace_emailu(self, email: str, index: int, soubor: str = 'manualni_vstup') -> str:
        """
        Overeni, zda-li je email platny.
        Args:
            email (str): Email k validaci.
            index (int): Index radku v CSV souboru.
            soubor (str): Nazev CSV souboru.
        Returns:
            str: Overeny email, nebo prazdny retezec, pokud neni platny.
        """
        if email:
            if not EMAIL_PATTERN.match(email):
                self.log.warning_message(f"Email '{email}' na radku c. {index} v souboru {soubor} je neplatny.")
                return ''
        else:
            self.log.warning_message(f"Na radku c.{index} v souboru {soubor} chybi email.")
            return ''
        return email

    def validace_telefonu(self, telefon: str, index: int, soubor: str = 'manualni_vstup') -> str:
        """
        Overeni, zda-li je telefon platny.
        Args:
            telefon (str): Telefon k validaci.
            index (int): Index radku v CSV souboru.
            soubor (str): Nazev CSV souboru.
        Returns:
            str: Overeny telefon, nebo prazdny retezec, pokud neni platny.
        """
        if telefon:
            if not PHONE_PATTERN.match(telefon):
                self.log.warning_message(
                    f"Telefon '{telefon}' na radku c. {index} v souboru {self.soubor} je neplatny.")
                return ''
            elif PHONE_PATTERN.match(telefon) and len(telefon) == 9:  # pokud chybi predvolba, pripojime
                self.log.info_message(
                    f"Telefonu '{telefon}' na radku c. {index} v souboru {self.soubor} byla doplnena chybejici predvolba.")
                return '+420' + telefon
        else:
            self.log.warning_message(f"Na radku c.{index} v souboru {self.soubor} chybi telefon.")
            return ''
        return telefon

    def validace_jmena(self, jmeno: str, index: int, soubor: str = 'manualni_vstup') -> str:
        """
        Overeni, zda-li je jmeno platne.
        Args:
            jmeno (str): Jmeno k validaci.
            index (int): Index radku v CSV souboru.
            soubor (str): nazev CSV souboru.
        Returns:
            str: Overene jmeno, nebo prazdny retezec, pokud neni platne.
        """
        if jmeno:
            if not all(prvek.isalpha() or prvek.isspace() or prvek == '-' for prvek in jmeno):
                self.log.warning_message(f"Jmeno '{jmeno}' na radku c. {index} v souboru {self.soubor} je neplatne.")
                return ''
        else:
            self.log.warning_message(f"Na radku c.{index} v souboru {self.soubor} chybi jmeno.")
            return ''
        return jmeno

    def validace_prijmeni(self, prijmeni: str, index: int, soubor: str = 'manualni_vstup') -> str:
        """
        Overeni, zda-li je prijmeni platne.
        Args:
            prijmeni (str): Prijmeni k validaci.
            index (int): Index radku v CSV souboru.
            soubor (str): nazev CSV souboru.
        Returns:
            str: Overene prijmeni, nebo prazdny retezec, pokud neni platne.
        """
        if prijmeni:
            if not all(prvek.isalpha() or prvek.isspace() for prvek in prijmeni):
                self.log.warning_message(
                    f"Prijmeni '{prijmeni}' na radku c. {index} v souboru {self.soubor} je neplatne.")
                return ''
        else:
            self.log.warning_message(f"Na radku c.{index} v souboru {self.soubor} chybi prijmeni.")
            return ''
        return prijmeni

    def validace_rozliseni(self, rozliseni: str, index: int, soubor: str = 'manualni_vstup') -> str:
        """
        Overeni, zda-li je rozliseni platne.
        Args:
            rozliseni (str): Rozliseni k validaci.
            index (int): Index radku v CSV souboru.
            soubor (str): nazev CSV souboru.
        Returns:
            str: Overene rozliseni, nebo prazdny retezec, pokud neni platne.
        """
        if rozliseni is None or not isinstance(rozliseni, str):
            self.log.warning_message(
                f"Rozliseni '{rozliseni}' na radku c. {index} v souboru {self.soubor} je neplatne.")
            return ''
        return rozliseni

    def kontrola_duplicity(self, jmeno: str, prijmeni: str, rozliseni: str) -> bool:
        """
        Provadi kontrolu, zda-li kontakt se zadanymi atributy jiz existuje.
        Args:
          **kwargs: Klicove argumenty pro atributy kontaktu (jmeno, prijmeni, rozliseni, email, telefon).
        Returns:
            bool: True pokud kontakt jiz existuje, jinak False.
        """
        for kontakt in self.kontakty:
            if (kontakt['jmeno'] == jmeno and
                    kontakt['prijmeni'] == prijmeni and
                    (kontakt['rozliseni'] == rozliseni or (not rozliseni and not kontakt['rozliseni']))):
                return True
        return False

    def nacist_a_validovat_kontakty(self) -> list:
        """
        Nacita kontakty ze souboru a  provadi normalizaci a validaci.
        Pokud jsou data validni, prida kazdy radek CSV souboru jako slovnik do seznamu.
        Returns:
            list: Seznam validnich kontaktu.
        Raises:
            ValueError: Pokud cesta k souboru neni nastavena.
        """
        if not self.soubor:
            self.log.error_message("Cesta k souboru neni nastavena.")
            raise ValueError("Cesta k souboru není nastavena!")

        pocet_kontaktu_csv = 0
        try:
            with open(self.soubor, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=',')

                for index, kontakt in enumerate(reader, start=2):
                    pocet_kontaktu_csv += 1

                    # Normalizace
                    normalizovany_kontakt = self.normalizace_dat(kontakt)

                    # Validace
                    jmeno = self.validace_jmena(normalizovany_kontakt['jmeno'], index, self.soubor)
                    prijmeni = self.validace_prijmeni(normalizovany_kontakt['prijmeni'], index, self.soubor)
                    rozliseni = self.validace_rozliseni(normalizovany_kontakt['rozliseni'], index, self.soubor)
                    email = self.validace_emailu(normalizovany_kontakt['email'], index, self.soubor)
                    telefon = self.validace_telefonu(normalizovany_kontakt['telefon'], index, self.soubor)

                    # Kontrola, aby se nepridal duplicitni kontakt
                    if self.kontrola_duplicity(jmeno, prijmeni, rozliseni):
                        self.log.info_message(f"Duplicitni kontakt na radku c. {index} nebyl pridan: {kontakt}.")
                        continue

                    # Nakonec pridani kontaktu pouze pokud ma jmeno/prijmeni a email/telefon
                    if (jmeno or prijmeni) and (email or telefon):
                        self.kontakty.append({
                            'jmeno':     jmeno,
                            'prijmeni':  prijmeni,
                            'rozliseni': rozliseni,
                            'email':     email,
                            'telefon':   telefon
                        })
                    else:
                        self.log.warning_message(f"Radek c.{index}: Neplatny kontakt: {kontakt}, -> Nebude ulozen!")

                print(
                    f"Bylo nacteno {len(self.kontakty)} platnych kontaktu z celkovych {pocet_kontaktu_csv} v databazi {self.soubor}.")
                self.log.info_message(
                    f"Bylo nacteno {len(self.kontakty)} platnych kontaktu z celkovych {pocet_kontaktu_csv} kontaktu v databazi {self.soubor}.")

        except Exception as e:
            self.log.error_message(f"Neocekavana chyba {e}!")

        return self.kontakty

    def setridit_kontakty(self) -> list:
        """
        Seradi kontakty nejprve podle prijmeni, pote podle jmena.
        Returns:
            list: Serazeny seznam kontaktu.
        """
        self.kontakty = sorted(self.kontakty, key=lambda x: (x['prijmeni'] or '', x['jmeno'] or ''))
        return self.kontakty

    def pridat_kontakt(self, **kwargs):
        """
        Prida kontakt do databaze ve fromatu **kwargs.
        Pred pridanim se provede normalizace a validace dat
        Kontakt se prida, pouze pokud ma alespon jmeno/prijmeni a alespon telefon/email.
        Rozliseni neni povinne.
        Args:
            **kwargs: Klicove argumenty pro jmeno, prijmeni, rozliseni, email a telefon.
        Returns:
            str: Zprava o vysledku pridani kontaktu.
        """

        # Normalizace
        normalizovany_kontakt = self.normalizace_dat(kwargs)

        # Validace
        jmeno = self.validace_jmena(normalizovany_kontakt.get('jmeno', ''), index=0)
        prijmeni = self.validace_prijmeni(normalizovany_kontakt.get('prijmeni', ''), index=0)
        rozliseni = self.validace_rozliseni(normalizovany_kontakt.get('rozliseni', ''), index=0)
        email = self.validace_emailu(normalizovany_kontakt.get('email', ''), index=0)
        telefon = self.validace_telefonu(normalizovany_kontakt.get('telefon', ''), index=0)

        if not (jmeno or prijmeni):
            self.log.warning_message(
                f"Chybi platne jmeno nebo prijmeni pro pridani kontaktu. Zadane parametry: {kwargs}.")
            return "Kontakt musi mit platne alespon jmeno nebo prijmeni."
        if not (email or telefon):
            self.log.warning_message(
                f"Chybi platny email nebo telefon pro pridani kontaktu. Zadane parametry: {kwargs}.")
            return "Kontakt musi mit platny alespon email nebo telefon."

        # Vytvoreni noveho kontaktu
        novy_kontakt = {
            'jmeno':     jmeno,
            'prijmeni':  prijmeni,
            'rozliseni': rozliseni,
            'email':     email,
            'telefon':   telefon
        }

        # Kontrola duplicity
        if self.kontrola_duplicity(jmeno, prijmeni, rozliseni):
            self.log.warning_message(f"Pokus o pridani jiz existujiciho kontaktu: {kwargs}.")
            return "Kontakt v databazi jiz existuje."

        # Pridani noveho kontaktu
        self.kontakty.append(novy_kontakt)
        self.log.info_message(f"Byl pridan novy kontakt: {novy_kontakt}.")
        return f"Byl pridan novy kontakt: {novy_kontakt}."

    def upravit_kontakt(self, index=None, **kwargs):
        """
        Upravi libovolny pocet hodnot kontaktu. Pred upravou provede normalizaci a validaci novych dat.
        Zabrani pridani duplicitniho kontaktu. Kontakt k uprave se specifikuje indexem.
        Args:
            index (int, optional): Index kontaktu k uprave.
            **kwargs: Klicove argumenty pro upravu kontaktu.
        Returns:
            str: Zpráva o výsledku úpravy kontaktu.
        """

        if index is not None:
            if index < len(self.kontakty):
                kontakt = self.kontakty[index]
            else:
                self.log.warning_message(f"Pri uprave kontaktu vyhledavani podle neexistujiciho indexu '{index}'.")
                return "Neplatny index"

            # Normalizace
            normalizovana_data = self.normalizace_dat({
                'jmeno':     kwargs.get('jmeno', kontakt['jmeno']),
                'prijmeni':  kwargs.get('prijmeni', kontakt['prijmeni']),
                'rozliseni': kwargs.get('rozliseni', kontakt['rozliseni']),
                'email':     kwargs.get('email', kontakt['email']),
                'telefon':   kwargs.get('telefon', kontakt['telefon'])
            })
            # Validace
            nove_jmeno = self.validace_jmena(normalizovana_data['jmeno'], index=index)
            nove_prijmeni = self.validace_prijmeni(normalizovana_data['prijmeni'], index=index)
            nove_rozliseni = self.validace_rozliseni(normalizovana_data['rozliseni'], index=index)
            novy_email = self.validace_emailu(normalizovana_data['email'], index=index)
            novy_telefon = self.validace_telefonu(normalizovana_data['telefon'], index=index)

            # Kontrola duplicity
            if self.kontrola_duplicity(nove_jmeno, nove_prijmeni, nove_rozliseni):
                self.log.warning_message(
                    f"Funkce upravit_kontakt neprobehla. Uprava kontaktu by zpusobila duplicitu: {kwargs}")
                return f"Duplicitni kontakt {kwargs}- uprava nebyla povolena."
            else:
                if 'jmeno' in kwargs:
                    kontakt['jmeno'] = nove_jmeno
                if 'prijmeni' in kwargs:
                    kontakt['prijmeni'] = nove_prijmeni
                if 'rozliseni' in kwargs:
                    kontakt['rozliseni'] = nove_rozliseni
                if 'email' in kwargs:
                    kontakt['email'] = novy_email
                if 'telefon' in kwargs:
                    kontakt['telefon'] = novy_telefon

                self.log.info_message(f"Byl upraven kontakt na indexu c.{index}.")
                return f"Kontakt na indexu c. {index} byl upraven."
        else:
            self.log.warning_message("Funkce upravit_kontakt neprobehla. Index nebyl zadan.")
            return "Index nebyl zadan."

    def ulozit_kontakty(self):
        """
        Ulozi kontakty do souboru CSV. Prepise obsah souboru.
        Returns:
            None
        """

        with open(self.soubor, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=DATA_SLOUPCE)
            writer.writeheader()

            for kontakt in self.kontakty:
                writer.writerow({
                    'jmeno':     kontakt.get('jmeno', ''),
                    'prijmeni':  kontakt.get('prijmeni', ''),
                    'rozliseni': kontakt.get('rozliseni', ''),
                    'email':     kontakt.get('email', ''),
                    'telefon':   kontakt.get('telefon', '')
                })
        self.log.info_message(f"Celkem {len(self.kontakty)} kontaktu bylo uspesne ulozeno do souboru {self.soubor}.")
        print(f"Kontakty byly uspesne ulozeny do souboru {self.soubor}.")

    def smazat_kontakt(self, index=None, jmeno=None, prijmeni=None, rozliseni=None):
        """
        Smaze kontakt z databaze na zaklade indexu nebo kombinace jmena/prijmeni/rozliseni.
        V pripade, ze je dane jmeno a prijmeni v databazi jen jednou, smaze ho i bez rozliseni. Pokud se opakuje, je nutno specifikovat i rozliseni.
        Args:
            index (int, optional): Index kontaktu k odstraneni.
            jmeno (str, optional): Jméno kontaktu k odstraneni.
            prijmeni (str, optional): Prijmeni kontaktu k odstraneni.
            rozliseni (str, optional): Rozliseni kontaktu k odstraneni.
        Returns:
            str: Zprava o uspesnem/ neuspesnem smazani.
        """

        # Pokud je zadany index
        if index is not None:
            try:
                smazany_kontakt = self.kontakty.pop(index)
                self.log.info_message(f"Byl odstranen kontakt {smazany_kontakt}.")
                return f"Kontakt {smazany_kontakt} byl odstranen."
            except IndexError:
                self.log.warning_message(f"Funkce smazat_kontakt neprobehla. Neplatny index: {index}.")
                return f"Neplatny index: {index}"

        # Mazani podle jmena, prijmeni a rozliseni
        if jmeno and prijmeni:
            shodne_kontakty = [kontakt for kontakt in self.kontakty
                               if kontakt['jmeno'].lower() == jmeno.lower() and
                               kontakt['prijmeni'].lower() == prijmeni.lower()]
            if len(shodne_kontakty) > 1:
                if rozliseni is None:
                    self.log.warning_message(
                        f"Funkce smazat_kontakt neprobehla. V databazi vice kontaktu se shodnym jmenem a prijmenim: {jmeno} {prijmeni}.")
                    return f"Nelze smazat kontakt pouze podle jmena a prijmeni, v databazi se opakuje. Specifikujte rozliseni."

            for index, kontakt in enumerate(self.kontakty):
                if (kontakt['jmeno'].lower() == jmeno.lower() and
                        kontakt['prijmeni'].lower() == prijmeni.lower() and
                        (rozliseni is None or kontakt['rozliseni'] == rozliseni)):
                    smazany_kontakt = self.kontakty.pop(index)
                    self.log.info_message(f"Kontakt {smazany_kontakt} byl odstranen.")
                    return f"Kontakt {smazany_kontakt} byl odstranen."

            self.log.warning_message(
                f"Funkce smazat_kontakt neprobehla. Kontakt s parametry: '{jmeno}','{prijmeni}','{rozliseni}' neexistuje.")
            return "Kontakt nebyl nalezen."

        self.log.warning_message(
            "Funkce smazat_kontakt neprobehla. Chybi parametr index nebo kombinace jmeno a prijmeni.")
        return "Pro smazani je treba zadat bud index, nebo kombinaci jmeno a prijmeni."

    def porovnej_shodu_vsech_parametru(self, kontakt: dict, **kwargs) -> bool:
        """Porovna, zda dany kontakt odpovida zadanym parametrum
        Args:
            kontakt (dict): Polozka kontaktu v databazi.
            **kwargs: Parametry pro porovnani.
        Returns:
            bool: True, pokud se shoduje. False, pokud ne.
        """
        for klic, hodnota in kwargs.items():
            if klic not in kontakt.keys() or (hodnota is not None and kontakt[klic].lower() != str(hodnota).lower()):
                return False
        return True

    def najit_kontakt(self, **kwargs) -> list:
        """
        Najde a vrati kontakt podle libovolne kombinace parametru.
        Vrati seznam nalezenych kontaktu dle kriterii.
        Args:
            *kwargs: Libovolne parametry pro hledani (jmeno, prijmeni, rozliseni, email, telefon)
        Returns:
            list: Seznam nalezenych kontaktu nebo zprava, ze nebyly nalezeny zadne kontakty.
        """
        nalezene_kontakty = [(index, kontakt) for index, kontakt in enumerate(self.kontakty) if
                             self.porovnej_shodu_vsech_parametru(kontakt, **kwargs)]
        if nalezene_kontakty:
            return nalezene_kontakty
        else:
            self.log.info_message(f"Funkci najit_kontakt se nepodarilo vyhledat kontakt dle zadanych parametru.")
            return "Zadana kriteria neodpovidaji zadnemu z kontaktu"

    def _tisk_tabulky(self, label: str, value: str):
        """
        Vytiskne naformatovanou tabulku pro zobrazeni vizitek.
        Args:
            label (str): Popis hodnoty.
            value (str): Hodnota k vytištění.
        Returns:
            None
        """

        # Delka hodnoty
        len_value = len(value) if value else 0

        # Zarovname label na fixni delku
        formated_label = f"{label:<{SIRKA_SLOUPCE_2}}"

        # Vypocitat chybejici vypln mezerami pro dany radek
        mezery = SIRKA_SLOUPCE_1 - SIRKA_SLOUPCE_2 - len_value - 5  #
        print(f"| {formated_label}| {value}{' ' * mezery}|")

    def detail_kontaktu(self, index=None):
        """
        Vypise vizitku kontaktu pomoci funkce _tisk_tabulky dle zadaneho indexu.
        Args:
            index (int, optional): Index kontaktu k zobrazeni.
        Returns:
            None
        """
        if index is not None:
            if index < len(self.kontakty):
                kontakt = self.kontakty[index]
                print('-' * SIRKA_SLOUPCE_1)
                self._tisk_tabulky('Jmeno', kontakt.get('jmeno'))
                self._tisk_tabulky('Prijmeni', kontakt.get('prijmeni'))
                if kontakt['rozliseni']:
                    self._tisk_tabulky('Rozliseni', kontakt.get('rozliseni'))
                self._tisk_tabulky('Email', kontakt.get('email'))
                self._tisk_tabulky('Telefon', kontakt.get('telefon'))
                index = self.kontakty.index(kontakt)
                self._tisk_tabulky('Index', str(index))
                print('-' * SIRKA_SLOUPCE_1)
            else:
                self.log.warning_message(
                    f"Funkce detail_kontaktu neprobehla. Index {index} je mimo rozsah seznamu kontaktu.")
                print(f"Index {index} je mimo rozsah seznamu kontaktu.")

    def vypsat_kontakty(self):
        """
        Vypise vsechny kontakty pomoci funkce detail_kontaktu.
        Returns:
            None
        """
        if not self.kontakty:
            self.log.warning_message(f"Funkce vypsat_kontakty neprobehla. Databaze je prazdna.")
            print("Databaze je prazdna")
        for index, kontakt in enumerate(self.kontakty):
            self.detail_kontaktu(index)
