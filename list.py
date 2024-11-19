"""
List
"""
from time import sleep

from pokus import jmeno

seznam = [1, 2, 3, 4, 5]

osoba = ["Tomas", 25, "Praha"]

text = "AHOJ"

prvky = ['A', 'B', 'C']

y = ['A', 'B', 'C', 'A', 'B', 'A', '123']

jmena = ['Petr', 'Honza', 'Jiri', 'Jan', 'Zuzana']


print(11 // 2)
print(int(11/2))
print(10 % 3)

print(10 == 11)
print(10 != 11)

print("-------------------")
print("     AHOJ  ".strip())
print("-------------------")


print(y)
print([prvek for prvek in y if prvek != 'A'])

vysledek = ""
for jmeno in jmena:
    vysledek += jmeno + ", "
print(vysledek[:-2])

