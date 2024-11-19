"""
OOP - objektove struktury
"""


class Osoba:
    """"""
    def __init__(self, jmeno, prijmeni, email, telefon, rozliseni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rozliseni = rozliseni
        self.email = email
        self.telefon = telefon
        self.__id = 0

    def cele_jmeno(self):
        """"""
        existuje_rozliseni = f" ({self.rozliseni})" if self.rozliseni else ""
        return f"{self.jmeno} {self.prijmeni}{existuje_rozliseni}"

    def popisny_nazev(self):
        """"""
        return f"{self.cele_jmeno()}, Tel: {self.telefon}, Email: {self.email}"

    def __str__(self):
        """"""
        return self.cele_jmeno()

    def __repr__(self):
        return self.popisny_nazev()

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def _napul_privatni(self):
        print("NAPUL PRIVATNI")

    def __uplne_privatni(self):
        print("UPLNE PRIVATNI")

    def tisk_uplne_privatni(self):
        self.__uplne_privatni()


class Zamestnanec(Osoba):
    def __init__(self, jmeno, prijmeni, email, telefon, rozliseni, oddeleni):
        super().__init__(jmeno, prijmeni, email, telefon, rozliseni)
        self.oddeleni = oddeleni

    def __repr__(self):
        """"""
        return f"{self.popisny_nazev()}, Oddeleni: {self.oddeleni}"


data = {
    'jmeno': 'Jan',
    'prijmeni': 'Novak',
    'email': "homer@simpsons.com",
    'telefon': "+420603603603",
    'rozliseni': "ml.",
    'oddeleni': "uctarna"
}

o = Osoba(jmeno='Jan',
          prijmeni='Novak',
          email="homer@simpsons.com",
          telefon="+420603603603",
          rozliseni="ml.")

print("ID: ", o.get_id())
x = Zamestnanec(**data)

print(repr(o), type(o))
print(repr(x), type(x))

print("ID: ", x.get_id())
x.set_id(100)
print("ID: ", x.get_id())

x._napul_privatni()
x.tisk_uplne_privatni()
