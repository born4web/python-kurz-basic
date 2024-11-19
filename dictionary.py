"""
Dictionary - slovnik
"""
import copy

slovnik = {}   # nebo dict(1,2,3)

# dict -- json
adresa = {
    "ulice": "Husova",
    "cislo": 123,
    "mesto": "Praha",
}
osoba = {
    "jmeno": "Tomas",
    "prijmeni": "Hrdina",
    "vek": 25,
    "adresa": adresa,
    "miry": [180, 90],
}
print(osoba)


x = dict(a=1, b=2, c=3, jmeno="Tomas", vek=25)

a = [1, 2]
b = ["A", "B", "C"]

print(dict(zip(a, b)))

