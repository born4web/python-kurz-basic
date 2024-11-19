""""""

klice = 'abcd'
hodnoty = (1, 2, 3)
neco = [10, 20]

seznam = zip(klice, hodnoty)
print(seznam, type(seznam))

print("poprve")
for prvek in seznam:
    print(prvek)

print("podruhe")
for prvek in seznam:
    print(prvek)
