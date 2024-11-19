"""

[vyraz for prvek in seznam if podminka]


"""

numbers = [1, -2, 3, 4, 0, 4, -5, 6, -7, -2]

slova = ['ahouj', 'jako', 'se', 'mas']


jen_kladna1 = [prvek for prvek in numbers if prvek >= 0]
jen_kladna2 = {prvek for prvek in numbers if prvek >= 0}
jen_kladna3 = (prvek for prvek in numbers if prvek >= 0)
print(jen_kladna1)
print(jen_kladna2)
print(jen_kladna3)
