""""""
"""
osoba = {
    "jmeno": "Petr",
    "prijmeni": "Vlcek",
    "vek": 30,
    "povolani": "prigr",
}

zajmy = {
    "sport": True,
    "vzdelani": "VS",
    "jmeno": "Honza",
}


spojeny = {**osoba, **zajmy}
print(spojeny)


def tisk_osoby(sport, vzdelani, jmeno):
    print("sport: ", sport)
    print("vzdelani: ", vzdelani)
    print("jmeno: ", jmeno)


tisk_osoby("fotbal", "VS", "petr")
tisk_osoby(**zajmy)
"""
import copy


data = {
    "jmeno": "Petr",
    "prijmeni": "Vlcek",
    "vzdelani": {
        "roky": 9,
        "typ": "VS",
        "skola": "VUT"
    },
    "vek": 30,
    "miry": [100, 200]
}

osoba = ["petr", "vlcek", "30"]

karta = {
    "id": 101,
    "person": osoba,
    "skola": "VS"
}
nova_karta = copy.deepcopy(karta)
napul_karta = karta.copy()

print(karta)
print(nova_karta)
print(napul_karta)
print("------")

karta["skola"] = "ZS"
nova_karta["person"][0] = "jindra"
napul_karta["person"][0] = "pavel"
napul_karta["id"] = 222
print(karta)
print(nova_karta)
print(napul_karta)
print("------")
print(osoba)

print("osoba id: ", id(osoba))
print("karta id: ", id(karta["person"]))
print("nova_karta id: ", id(nova_karta["person"]))
print("napul_karta id: ", id(napul_karta["person"]))



osoba = {
    "jmeno":    "Petr",
    "prijmeni": "Vlcek",
    "vek":      30,
    "miry":     [100, 200],
}

# nacetl jsem radk ze souboru
zaznam1 = {
    "jmeno":    "Petr",
    "prijmeni": "Vlcek",
    "vek":      30,
    "miry":     [100, 200],
}

# inicializuji prazdnou promenou
osoba = {
    "jmeno":    "",
    "prijmeni": "",
    "vek":      0,
    "miry":     [],
}

# naplnim mou promenou daty ze soubopru
osoba.update(zaznam1)

# a ted data zacinam zpracovavat
