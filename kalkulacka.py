"""
vytvorit dict s klicy matematickych operace a prislusne funkce pro operaci se dvema cisly

'+' '-' '*' '/'
"""

def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def krat(x, y):
    return x * y


def deleno(x, y):
    return x / y


kalkulacka = {
    '+': plus,
    '-': minus,
    '*': krat,
    '/': deleno
}

print(kalkulacka['+'](1, 2))
print(kalkulacka['-'](1, 2))
print(kalkulacka['*'](1, 2))
print(kalkulacka['/'](1, 2))


