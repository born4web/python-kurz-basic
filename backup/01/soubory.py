"""
cesta:  /adresar1/adresar/data/moje/txt/mujdopis.txt
        C:\\Users\\adresar\\test.txt

        adresar / adresar / mujdopis.txt


rezim prace:   r - read  w - write  a - append b - binary

# Nactu obsah souboru cely do listu po radcich
with open('mojedata.txt', 'rb') as file:
    obsah = file.readlines()
    # print(obsah)

# print(obsah)

with open('mojedata.bak', 'wb') as file:
    file.write(b"ZALOHA DAT MOJEDATA.TXT\n")
    file.writelines(obsah)

# utf-8
text = "Třista třicet stříkaček čelo omývalo"
kodovany_text = text.encode('utf-8')
obnoveny_text = kodovany_text.decode('utf-8')
print(text)
print(kodovany_text)
print(obnoveny_text)

# novy soubor vytvoreny
with open("pozdrav.txt", "w") as file:
    file.write("Ahoj vsichni!")


# program bezi pridej text do souboru
with open("pozdrav.txt", "a") as file:
    file.write("\nJak se mate?")


# program bezi vypis soubor
with open("pozdrav.txt", "r") as file:
    obsah = file.read()
    print(obsah)


with open("pozdrav.txt", "r") as file:
    i = 1
    for line in file:
        print(i, line.strip())
        i += 1

mesta = ["Praha", "Brno", "Ostrava", "Plzeň", "Liberec"]
vesnice = ["Bezdikov", "Frycovice", "Brusperk"]

with open("mesta.txt", "a") as file:
    for kazdou in vesnice:
        file.write(kazdou+"\n")
"""


with open("slozenina.txt", "w") as outfile:
    f_mesta = open("mesta.txt", "r")
    f_pozdrav = open("pozdrav.txt", "r")
    mesta_data = f_mesta.readlines()
    pozdrav_data = f_pozdrav.readlines()
    f_mesta.close()
    f_pozdrav.close()
    i = 0
    while i < len(mesta_data):
        outfile.write(mesta_data[i])
        outfile.write(pozdrav_data[i])
        i += 1


with (open("data.csv", "r") as datafile,
      open("data2.csv", "r") as csvfile,
      open("mesta.txt", "r") as mestafile):
    print(datafile.read())
    print(csvfile.read())
    print(mestafile.read())




