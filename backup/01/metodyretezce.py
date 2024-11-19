""""""
"""
s = 'ahOj kAMArade jaK se MAS'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print("-----------------\n", s)

x = '    Ahoj kamarade    \n'
print(x)
print(x.lstrip())
print(x.rstrip())
print(x.strip())
"""

y = 'Ahoj programatore Python skvele programuje'

print(y)
"""stary = 'Ahoj'
novy = 'Hello'
print(y.replace(stary, novy))
print(y.find('prog'))
print(y.rfind('prog'))
print(y.rfind('prog', 0, 10))
print(y.count('Pyt'))
"""

print(y.split(' ', 2))
print(y.rsplit(' ', 2))

deleny = y.split(' ')
print(deleny)
zpet = '-'.join(deleny)
print(zpet)

data = ' Petr;Vlcek;CodingSchool ;182 ;homer@simpsons.com'
print(data.split(';'))

print(len(y.split()))

soubor = "/home/pvlcek/data/documents/test.txt"
linux = soubor.split('/')
windows = "\\".join(linux)
print("c:\\" + windows)

