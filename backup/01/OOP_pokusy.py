"""
Log soubor pro podporu projektu

1. standardne bude soubor error.log
2. log_file.py knihovna pro praci s logem
3. kazdy zaznqam logu bude vypadat:
    ---------------------------------------------------
    datum, cas, error/warning/info, vlastni text zpravy
    ---------------------------------------------------
"""
from datetime import datetime

LOG_FILE = "error.log"
ERROR_MESSAGE = "Error"
WARNING_MESSAGE = "Warning"
INFO_MESSAGE = "Info"
MESSAGE_DEVIDER = "---------------------------------------------------"
USE_MESAGE_DEVIDER = True


def tabulkove_zobrazeni_osoby(jmeno, prijmeni, vek):
    print(f"Jmeno: {jmeno}")
    print(f"Prijmeni: {prijmeni}")
    print(f"Vek: {vek}")


class Osoba:
    """
    Osoba
    """
    def __init__(self, jmeno="", prijmeni="", vek=0):
        """"""
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def __str__(self):
        """"""
        return self.full_name()

    def __repr__(self):
        """"""
        return f"jmeno={self.jmeno}, prijmeni={self.prijmeni}, vek={self.vek}"

    @property
    def is_senior(self):
        """Senior vek > 65 -> True jinak false

        """
        if self.vek > 65:
            return True
        else:
            return False

    @staticmethod
    def casova_znacka():
        """casova znacka"""
        return datetime.now()

    def jen_jmeno(self):
        return f"{self.jmeno} {self.prijmeni}"

    def prijmeni_jmeno(self):
        return f"{self.prijmeni} {self.jmeno if self.jmeno else '-'}"

    def full_name(self):
        return f"{self.jmeno} {self.prijmeni} ({self.vek})"

    def tisk_jmeno_tabulka(self):
        tabulkove_zobrazeni_osoby(self.jmeno, self.prijmeni, self.vek)


class Pracovnik(Osoba):
    """"""
    def __init__(self, funkce, jmeno="", prijmeni="", vek=0):
        """"""
        super().__init__(jmeno, prijmeni, vek)
        self.funkce = funkce
        self.senior = self.senior_junior()

    def senior_junior(self):
        """"""
        if self.vek > 50:
            return True
        else:
            return False


d = Pracovnik('vedouci', 'Jana', 'Bergl', 70)

print(d.jmeno)
print(d.prijmeni)
print(d.vek)
print(d.funkce)

d.tisk_jmeno_tabulka()

print(d.prijmeni_jmeno())


