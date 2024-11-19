"""
Kalkulacka

slovnik funkci pracujici se dvema parametry x, y

funkce budou plus "+", minus "-", krat "*", deleno "/"

kalkulacka["/"](x, y)

"""


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def krat(x, y):
    return x * y


def deleno(x, y):
    return x / y if y != 0 else "nulou nelze delit"


kalkulacka = {
    "+": plus,
    "-": minus,
    "*": krat,
    "/": deleno,
}

print(kalkulacka["+"](2, 3))
print(kalkulacka["/"](y=0, x=2))


