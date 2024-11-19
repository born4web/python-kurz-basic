
# type hitting

cislo = 123

promena = {"jmeno": "Petr", "prijmeni": "vlcek", "vek": 34}
# jednoduche datove typy int, float, str, bool -> True/False
# kolekce list, tuple, set, dict
# super slozite -> objekty class

# PEP8
# snake_case
moje_data = {"jmeno": "Petr", "prijmeni": "vlcek", "vek": 34}

udaj = "jmeno"
udaje = ["jmeno", "prijmeni", "vek"]

SIRKA_RADKU = 80

# mutable = zmenitelne list, set, dict
# immutable = nezmenitelne  int, float, str, tuple

a = "abcd"
b = a

print(a)
print(b)
print(type(a))
print(type(b))
print(id(a))
print(id(b))

b = "efgh"
print(a)
print(b)
print(id(a))
print(id(b))
print("---------------------------")
seznam = [1, 2, 3]
kopie = seznam
print(seznam)
print(type(seznam))
print(id(seznam))

seznam.append(4)
print(seznam)
print(id(seznam))


