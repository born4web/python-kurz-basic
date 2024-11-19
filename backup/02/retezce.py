""""""

s = 'ahoj-kamarade jak se mas'
c = '0123456789012345678901234567890123456789'

print("vysledek:", c[::-1])

jmeno = "|Ing. |Petr      |Vlcek     |Csc. |"
jmeno = "|     |Pavel     |Bocek     |     |"

jen_jmeno = jmeno[8:20]
jen_prijmeni = jen_jmeno[11:21]

jen_prijmeni = jmeno[8:20][11:21]

x = '12a34b56c78d'
print(x[2::3])

# I.
jen_cisla = x[0:2] + x[3:5] + x[6:8] + x[9:11]

# II. nahradime znaky co nechceme ''
jen_cisla = x.replace('a', '').replace('b', '').replace('c', '').replace('d', '')

# III. comprehension
jen_cisla = [znak for znak in x]
jen_cisla = ''.join([znak for znak in x if znak.isdigit()])

print(jen_cisla)




