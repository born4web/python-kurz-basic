jedny_uvozky = 'jednoduche'
dvojite_uvozovky = "dvojite"
trojite = """
AHoj 
mame vice
radku textu
"""
abeceda = "abcdefghijklmnopqrstuvwxyz"
desitka = "0123456789"
# print(id(test))

# slicing pokusy
# zacatek = 1
# konec = len(cisla)
# krok = 2
# print(cisla[zacatek:konec:krok])

# skladani retezcu
# s1 = "Ahoj"
# s2 = "mas"
# vysledek = s1 + " jak se " + s2
# print(s1, " jak se ", s2, "!")
# print(vysledek)

# deleni a skladani retezcu
# pozdrav = "Ahoj chlape jak se vede!"
# print(pozdrav)
# sl = pozdrav.split(" ", 1)
# print(sl)
# sr = pozdrav.rsplit(" ", 1)
# print(sr)
# print("XYZ".join(sl))

# vyhledavani a nahrazovani podretezcu
# s = "Hello world world world"
# print(s.replace("world", "Python"))

# Velikosti pismen
# s = "Ahoj PArdE"
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

# formatovani retezcu
jmeno = "Pepo"
vek = 50
print(f"""Ahoj {jmeno} jak se mas {vek}tniku""")
print("Ahoj {} jak se mas {}tniku".format(jmeno, vek))
print("Ahoj {1} jak se mas {0}tniku".format(vek, jmeno))

print("Ahoj %s jak se mas %d tniku" % (jmeno, vek))





