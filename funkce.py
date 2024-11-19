"""
Funkce

def nazev_funkce(parametry):
....kod ktery se provede
    return hodnotu co vracim

  None - nic nevracim
"""
PARAMETR = "------"


def druha_mocnina(cislo: int) -> int:
    """Druha mocnina

    :param cislo: zadej cioslo ktere se umocnit na 2
    :return: druha mocnina cisla
    """
    return cislo ** 2


def tisk_visitky():
    print("Petr, Vlcek, lektor")
    print(PARAMETR)


def vizitka(jmeno, prijmeni="Novak", vek=25):
    print(f"Jmeno: {jmeno}\nPrijmeni: {prijmeni}\nVek: {vek}")  # print(jmeno, prijmeni, vek)


# vizitka("Petr", vek=25)


# sberne paramtery
# *args - promenny pocet pozicnich parametru
# **kwargs - promenny pocet klicovych parametru

def pozicni_parametry(*args):
    print(args)
    print(args[0])


def secti_vsechna_cisla(*args):
    soucet = 0
    for cislo in args:
        soucet += cislo
    return soucet


def klicove_parametry(**kwargs):
    print(kwargs)

parametry = {
    "jmeno": "Tomas",
    "prijmeni": "Hrdina",
    "vek": 25
}


def prevod_stupnu_fahrenheit(*args):
    """Prevadime jeden nebo vice hodnot C na F

    20 - 50 C   -  normqalni teplota N
    <20  -  nizka teplota  L
    >50  -  vysoka teplota H

    [(20-50,68,'N'), (>50, 212, 'H'), (<20, 32, 'L)]

    'N' normalni hodnota,  'L' nizka, 'H' vysoka
    """
    vysledky = []

    def c_2_f(c):
        """Srtupne na F (c * 9/5) + 32"""
        return (c * 9 / 5) + 32

    for cislo in args:
        prevod = [cislo, c_2_f(cislo)]
        if cislo < 20:
            prevod += ["L"]
        elif cislo > 50:
            prevod += ["H"]
        else:
            prevod += ["N"]
        vysledky.append(tuple(prevod))
    return vysledky


prevod_cidla = prevod_stupnu_fahrenheit

print(prevod_cidla(0, 50, 200))


def mocnina(cislo):
    return cislo ** 2

def krat2(cislo):
    return cislo * 2


def vypocet(funkce, cislo):
    return funkce(cislo)


