"""
Seznameni se s ruznymi datovymi typy v Pythonu
# int, float, bool, str, list, tuple, set, dict

pokusy s promenymi a vystupy
"""


a = 0
b = 10.5
c = 1 + 2j
pravda = False
retezec = 'kamarade'

# list
osoba = ["petr", "vlcek", 35, 80] # mutable
x = range(10)  # for cyklus

# tuple
karta_klienta = ("petr", "vlcek", 35, 80) # unmuablee

# set
data = [1, 2, 3, 2, 5, 6, 1, 2]

# dict
databanka = {"prijmeni": "vlcek", "vek": 34, "jmeno": "Petr"}

print(databanka)
print(data[0])
print(databanka["prijmeni"])
