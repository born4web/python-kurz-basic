"""
if 1.podminka:
    Splnena 1. toto se udela
# VYSKA OSOBY
x = 0
if x >= 200:
    print(f"Pozor jsi obr neprojdes dvermi")
elif x > 180:
    print(f"to jsi vysoky")
elif x > 150:
    print(f"ale jo to by jeste slo")
elif x > 80:
    print(f"hele jsi docela maly")
else:
    print("Nesplneno nic")

# VYHODNOCUJI VICE PARAMETRU SOUCASNE
vyska = 120  # maly / velky
boty = 25  # male / velke
vlasy = 30  # 0-50 svetle jinak tmave

vysledek = {
    "vyska": "prumerna",
    "vlasy": "cervene",
    "boty": "zadne",
}

# Vyska 150+
if vyska > 150:
    vysledek["vyska"] = "velky"
else:
    vysledek["vyska"] = "maly"
if boty > 40:
    vysledek["boty"] = "velke"
else:
    vysledek["boty"] = "male"
if vlasy > 50:
    vysledek["vlasy"] = "tmave"
else:
    vysledek["vlasy"] = "svetle"

print(vysledek)

postava = ["mala", "stredni", "vysoka"]
frantisek_vyska = "je to stramak"
frantisek_vyska = "mala11"

if frantisek_vyska in postava:
    print("data OK")
else:
    print("CHYBA DAT")
if frantisek_vyska == "mala":
    print("Data OK")
elif frantisek_vyska == "stredni":
    print("Data OK")
elif frantisek_vyska == "vysoka":
    print("Data OK")
else:
    print("CHYBA DAT")


vzdelani = ["zakladni", "stredni", "vysokoskolske"]
majetek = ["chudy", "stredni", "bohaty"]
vyska = 150  # 0-250 cm  ostatni hodnoty nebereme

frantisek_vzdelani = ""
if frantisek_vzdelani in vzdelani:
    print(f"Vzdelani uvedeno: {frantisek_vzdelani}")
else:
    print(f"Vzdelani neuvedl")

print(frantisek_vzdelani if frantisek_vzdelani in vzdelani else "neuvedl")

# PODMINKY

x = -2
vysledek = "kladne" if x >= 0 else "zaporne"
print(f"X je {vysledek} cislo")

cisla = [1, 2, 3]
x = 2
if x in cisla:
    print(f"{x} je v seznamu")
else:
    print(f"{x} neni v seznamu")

d = {'a': 1, 'b': 2, 'c': 3}
key = 'd'
if key in d:
    print(f"Klic '{key}' je v seznamu")
else:
    print(f"Klic '{key}' neni v seznamu")

a = 10
b = 10
c = 10
if a == c == b:
    print("cisla jsou stejna")

print("konec programu")

a = 10
b = "ahoj"
if str(a) > b:
    print(f"a vetsi b")
else:
    print(f"a mensi b")


print(type(a), type(b))

if type(a) == type(1.2):
    print("a je int")
else:
    print("a NENI int")
if isinstance(a, int):
    print("a je int")
"""

typy_postav = ["mala", "stredni", "vysoka"]
rozsah_vysek = [25, 250]
vaha = 80  # kladne cislo
pohlavi = ["M", "Z"]

osoba = {
    "pohlavi": "M",
    "vyska": 180,
    "vaha": 100,
    "typ_postavy": "stredni",
}


print("-------------------")
# pohlavi
if osoba["pohlavi"]:
    if osoba["pohlavi"] in pohlavi:
        pass
    else:
        print("chyba neplatny udaj POHLAVI")
else:
    print("nezadana data POHLAVI")
# vyska
if osoba["vyska"]:
    if 25 < osoba["vyska"] < 250:
        pass
    else:
        print("chyba neplatny udaj VYSKA")
else:
    print("nezadana data VYSKA")
# vaha
if osoba["vaha"]:
    if osoba["vaha"] <= 0:
        print("chyba neplatny udaj VAHA")
else:
    print("nezadana data VAHA")
# typ postavy
if osoba["typ_postavy"]:
    if osoba["typ_postavy"] not in typy_postav:
        print("chyba neplatny udaj TYP POSTAVY")
else:
    print("nezadana data TYP POSTAVY")
print("-------------------")



