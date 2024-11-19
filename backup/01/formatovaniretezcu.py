""""""

jmeno = 'Petr'
prijmeni = 'Vlcek'
dokonceni_kurzu = 0.75

#print("Vitejte Jmeno:%s Prijmeni:%s" % (jmeno, prijmeni))

#print("Vitejte Jmeno:{1} Prijmeni:{0}".format(jmeno, prijmeni))
#print("Vitejte Jmeno:{name} Prijmeni:{surname}".format(name=jmeno, surname=prijmeni))

#print(f"| {jmeno:<20} | {prijmeni:^20} | {dokonceni_kurzu*100:.2f}% |")

cestina = 'čočka s párkem'
print(cestina)
kodovane = cestina.encode('utf-8')
print(kodovane)
print(kodovane.decode('utf-8'))

r = r"c:\data\text.txt\n"
print(r)
