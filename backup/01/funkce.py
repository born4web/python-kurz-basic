

# predam parameter ten se vytickne na obrazovku
def nazev_funkce(text_k_tisku="nejaky text"):
    """
    Testovaci funkce na demonstraci vytvareni funkce v Pythonu

    :param text_k_tisku:  Tet ktery se ma vyticknout na obrazovku

    :return:  nevraci nic
    """
    # vlastni kod funkce
    # kus programu ktery vykonam
    print(text_k_tisku)


def dva_parametry(a, b=2, c=3):
    print(a)
    print(b)
    print(c)


def pozdrav(osoba, text_pozdravu="Dobry den: "):
    print(f"{text_pozdravu} {osoba}")


def mocnina(cislo, mocnitel=2):
    return cislo ** mocnitel


def druha_mocnina(cislo):
    return mocnina(cislo)


def treti_mocnina(cislo):
    return mocnina(cislo, 3)


cisla = [-1, 2, 3, 100]

def minimum1(seznam_cisel):
    min = seznam_cisel[0]
    for cislo in seznam_cisel[1:]:
        if cislo < min:
            min = cislo
    return min


def min_max1(seznam_cisel):
    return min(seznam_cisel), max(seznam_cisel)


def min_max(seznam_cisel):
    minimum = seznam_cisel[0]
    maximum = seznam_cisel[0]
    for cislo in seznam_cisel:
        if cislo < minimum:
            min = cislo

    for cislo in seznam_cisel:
        if cislo < maximum:
            min = cislo

    return minimum, maximum

osoba = {
    'jmeno': "Franta",
    'prijmeni': "Vopicka",
    'vek': 55,
    'vaha': 100,
    'stav': "Zenaty"
}


def tisk_detailu_osoba(osoba):
    for key, value in osoba.items():
        print(f"{key.capitalize()}: {value}")


def vypocet_nad_seznamem(seznam_cisel, funkce):
    for cislo in seznam_cisel:
        print(f"{cislo} - {funkce(cislo)}")


def nadrazene_telo_funkce(seznam_cisel):

    def mocnina2(cislo):
        return cislo ** 2

    for cislo in seznam_cisel:
        print(f"cislo: {cislo}, druha mocnina: {mocnina2(cislo)}")


vek_osob = [25, 30, 43, 50, 60]

def prumerny_vek(veky):
    soucet = 0
    for cislo in veky:
        soucet += cislo
    return soucet / len(veky)


slova = ["pes", "kočka", "sloni kel", "hroch"]


def nejdelsi_slovo(seznam_predanych_slov):
    nejdelsi = seznam_predanych_slov[0]
    for slovo in seznam_predanych_slov:
        if len(slovo) > len(nejdelsi):
            nejdelsi = slovo
    return nejdelsi


print(nejdelsi_slovo(slova))

a = [1,2,3,4,5,6,7,8,9,10]

y = [x for x in a if x % 2 == 0]

print(y)



