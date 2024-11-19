"""
Podminky

if, elif, else

if logicka_podminka:
    blok programu    # ident


"""
x = 8
if x < 10:
    print(f"Prutok je: {x}, (manesi nez 10) -> je potreba OTEVRIT venti!")
elif x > 20:
    if x < 50:
        print(f"Prutok je: {x}, ( vetsi nez 20) -> je potreba UZAVRIT venti! ZLUTY ALARM")
        if x > 40:
            print("Hledej klic k ventilu RYCHLE")
    else:
        print(f"Prutok je: {x}, ( vetsi nez 50) -> HROZI KATASTROFA! CERVENY ALARM")
else:
    print(f"Prutok je: {x}, Vsechno OK!")


# podminky komplexni - not, and, or - menim toto poradi ()
print("-------------")
if 0 < x < 10 and x % 2 == 0:
    print("x je v rozsahu 0 a 10 a zaroven sude")

x = 11
y = 2
# x / y    10 / 3 = 3.33  3 * 3 = 9   10 - 9 = 1
# print(x % 2 != 0)