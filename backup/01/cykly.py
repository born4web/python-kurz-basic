slovo = "abcdefghij"
slovnik = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
mnozina = set("abcdefghijabcdefghijabcdefghij")
pocitadlo = 10

# vezmi seznam a vytiskni obracene poradi
# 1. print(seznam[::-1])
# for cislo in seznam[::-1]:
#   print(cislo)

# 2. seznam.reverse()
# for cislo in seznam[::-1]:
#   print(cislo)


# vezmi seznam a vytvor z nej novy pomoci cyklu s obracenym poradim prvku

seznam = [1, 2, 3, 4, 5]
listy = [[1, 2], [3, 4], [5, 6]]



# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# vysledek = [[1,2,3],[4,5,6],[7,8,9]]
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suda = []
# suda obsahovala suda cisla z seznamu cisla
for prvek in cisla:
    if prvek % 2 == 0:
        suda.append(prvek)
print(suda)

