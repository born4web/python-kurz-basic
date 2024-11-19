"""
LIST: [expression for item in iterable if condition]

[value_if_true if condition else value_if_false for item in iterable]

"""
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cisla = []
for i in range(1, 11):
    cisla.append(i)
print(cisla)

#cisla1 = [i for i in range(1, 11) if i % 2 == 0]
#print(cisla1)

#integer = [-1, -2, 2, 5]
# [(-1, '-'),...,(2, '+'),...]
#znamenko_cislo = [(x, '-' if x < 0 else '+') for x in integer]
#print(znamenko_cislo)

druha_mocnina = [i**2 for i in cisla]
words = ["apple", "banana", "cherry", "orange", "apple", "havana"]
velka = [i.upper() for i in words]
konci_na_a = [i for i in words if i[-1] == 'e']
konci_na_a = [i for i in words if i.endswith('e')]
delky_slov = [i for i in words if len(i) == 5]

# {key_expression: value_expression for item in iterable if condition}
delky_slov = {slovo: len(slovo) for slovo in words if len(slovo) == 6}
print(delky_slov)

x = {'a': 1, 'b': 2, 'c': 3}
y = {item[1]: item[0] for item in x.items()}
y = {value: key for key, value in x.items()}
print(y)

cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mocniny = {cislo: cislo**2 for cislo in cisla if cislo % 2 != 0 and cislo < 7}
print(mocniny)

integer = [-1, -2, 0, 2, 5]
znaminka = [(x, '-' if x < 0 else ('+' if x > 0 else '*')) for x in integer]
print(znaminka)

# matici 3x3
# [[1,2,3],
# [1,2,3],
# [1,2,3]]
numbers = [1, 2, 3, 4, 5]
pismena = ['a', 'b', 'c', 'd', 'e']
# seznam (1,'a'), (2,'b'),...

kombinace = [(l, k**2) for k,l in zip(numbers, pismena)]
print(kombinace)

list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]


mocniny_list = [x**2 for x in list1]
mocniny_set1 = set(mocniny_list)
mocniny_set2 = {x**2 for x in list1}
print(mocniny_list)
print(mocniny_set1)
print(mocniny_set2)