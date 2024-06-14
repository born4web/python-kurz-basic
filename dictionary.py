a = {}
b = {'a': 1, 'b': 2, 'c': 3}
c = {'e': 5, 'f': 6, 'a': 10}
print(b)

#print(b.keys())
#print(b.values())
#print(b.items())

d1 = {'jmeno': 'Franta', 'vek': 30}
d2 = {'ulice': 'Karlova 52', 'mesto': 'Mseno'}

osoba = {
    'jmeno': {'krestni': 'Franta', 'prijmeni': 'Vopicka'},
    'adresa': {'ulice': 'Karlova 52', 'mesto': 'Mseno'},
    'vek': 50,
    'miry': [180, 80],
    101: 'moje id',
    # ...
}

print(a)
a['jmeno'] = 'Pepa'
a.setdefault('jmeno', 'John Doe')
print(a)

x = [1, 2, 3, 4, 5]
x = ['jmeno', 40, ...]

x = ['jemno', 40]

