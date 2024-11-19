"""
Comprehension
- list, dict, set, "tuple"

[expression for item in iterable if condition]

{key_expression: value_expression for item in iterable if condition}

"""
slovnik = {"jmeno": "Tomas", "prijmeni": "Hrdina", "vek": 25}

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slova = ["ahoj", "pane", "jak", "se", "mas", "ahoj"]

suda = [cislo for cislo in cisla if cislo % 2 == 0]
mocnina = [cislo ** 2 for cislo in cisla]

velka_pismena = [kazde_slovo.upper() for kazde_slovo in slova]

delky_slov = [len(kazde_slovo) for kazde_slovo in slova if len(kazde_slovo) > 3]

slova_delka = {kazde_slovo: len(kazde_slovo) for kazde_slovo in slova}

index_slovnik = {slova.index(kazde_slovo): kazde_slovo for kazde_slovo in slova}

index_slovnik2 = {kazde_slovo[0]: kazde_slovo[1] for kazde_slovo in enumerate(slova)}

index_slovnik3 = {klic: hodnota for klic, hodnota in enumerate(slova) if klic % 2 != 0}


cisla = [1, 2, 2, 1, 3, 2, 4, 3, 5]
print(cisla)

print(set(cisla))

mnozina = (polozka for polozka in cisla if polozka % 2 != 0)
print(mnozina)
