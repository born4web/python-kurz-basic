
def soucet_cisel(*args):
    print(args)
    soucet = 0
    for cislo in args:
        soucet += cislo
    print(soucet)


soucet_cisel(1, 2, 3)


def pridej_kontakt(*args, **kwargs):
    print('*args: ', args)
    print('**kwargs: ', kwargs)


pridej_kontakt(10, 20, 'Ahoj', jmeno='Petr', prijmeni='Vlcek', vek=25)


def komplexni_funkce(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    ## NEPODSTATNE -> ZALEZI NA PROGARMU A PROGRAMATOROVI
    if args:
        senzor1 = args[0]
    print(senzor1)




merene_udaje = (10, 20, 30)
kontakt_data = {
    'd': 3,
    'jmeno': 'Vlcek',
    'prijmeni': 'Petr',
}
komplexni_funkce(1,2, *merene_udaje, **kontakt_data)


def pozdrav(jmeno, prijmeni, /, vek, *, text_pozdravu="Dobry den: ", email=None, telefon=None):
    print(f"{text_pozdravu}{jmeno} {prijmeni} {vek}")


# pozdrav(prijmeni='Vlcek', jmeno='Petr', text_pozdravu='Ahoj: ', vek=40)
pozdrav('Petr', 'Vlcek', vek=40)
