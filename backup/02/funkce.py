"""
Funkcemi

funkce ma parametry
v realnem case parametyry naplneny argumenty

def jmeno_funkce(a, b, jmeno):
    # blok programu
    return navratove_hodnoty

"""

slovnik_dat = {
    "jmeno": "honza",
    "prijmeni": "vlcek",
    "vek": 45,
}

# *args  *names *numvers
# **kwargs  **data **vizitky


def soucet_cisel(*args):
    """"""
    soucet = 0
    for x in args:
        soucet += x
    return soucet


def tisk_vizitky(**kwargs):
    """"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# print(soucet_cisel(1, 2, 3))
# tisk_vizitky(**slovnik_dat)

radek_souboru = ["petr", "vlcek", 50, "ahoj"]


def tisk_dat_ze_souboru(radky_souboru):
    """"""

    def zpracuj_data(jmeno, prijmeni, vek, pozdrav):
        """"""
        return {
            "jmeno":    jmeno.capitalize(),
            "prijmeni": prijmeni.capitalize(),
            "vek":      vek,
            "pozdrav":  pozdrav.title(),
        }

    def validate_data(data_slovnik):
        return data_slovnik

    for radek in radky_souboru:
        data_slovnik = zpracuj_data(*radek)
        validovana_data = validate_data(data_slovnik)
        print("------------------")
        print(validovana_data)
        print("------------------")


