# DATOVY TYP LIST

prazdny = []
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9]
retezce = ["Ahoj", "parde", "jak", "se", "mas"]
ruzne = ["jmeno", "prijmeni", 50, [180, 95], ["jmeno", "prijmeni"]]


# zmena prvku
# print(ruzne)
# jmeno = 'pepa'
# prijmeni = 'VomACka'
# ruzne = [jmeno, prijmeni, 50, [180, 95], ["jmeno", "prijmeni"]]
# ruzne[0] = jmeno.capitalize()
# ruzne[1] = prijmeni.capitalize()
# print(ruzne)

# pridani a ubirani prvku
print(ruzne)
# ruzne.append("Vaclavske nam. 1")
# ruzne.insert(2, "Vaclavske nam")

adresa = ["Vaclavske nam. 1", "Praha 1"]
var1 = ruzne[:]
var2 = ruzne[:]

var1.append(adresa)
var2.extend(adresa)
print(var1, len(var1))
print(var2, len(var2))

x = ruzne + ruzne + adresa

print(retezce)
retezce += retezce
print(retezce)

print(retezce.count("parde"))

print(retezce.index("mas"))






