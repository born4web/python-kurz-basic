"""
Cykly

for cyklus - iteraci pres sekvenci prvku

while cyklus - dokud je splnna podminka

"""
from time import sleep

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seznam = "AHOJ"

"""
for cislo in seznam:
    print(cislo)

for index, prvek in enumerate(seznam):
    print(index, prvek)


for x in range(1, 11, 2):   # range(zacatek vcetne, konec vyjma, krok)
    print(x)
"""

# cyklus while
pocitadlo = 0
while pocitadlo < 5:
    if pocitadlo == 8:
        break
    print(f"Iterace cyklu: {pocitadlo}")
    sleep(1)
    pocitadlo += 1
else:
    print("Cyklus skoncil v poradku")



