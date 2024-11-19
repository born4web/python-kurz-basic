"""
Lambda funkce


lambda argumenty: vyraz

"""


c_to_f = lambda c: c * 9 / 5 + 32
suma_abc = lambda a, b, c: a + b + c

druha_mocnina = lambda x: x ** 2


def druha_mocna_fce(x):
    return x ** 2





print(c_to_f(0))

print(list(map(lambda x: x * 2, [0, 10, 100])))

print(suma_abc(2,4,6))