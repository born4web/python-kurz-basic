'''

Programek procvicuje slovicka, ktera jsou nahrana v jednotlivych souborech:

HROMADKA_0  ->  Pracovni soubor, kam se ukladaji spatne odpovedi behem prubehu programu.
                Na zacatku a na konci musi byt prazdny.
HROMADKA_1  ->  Zde zacina procvicovani slovicek, zde se take nahravaji nova slovicka.
HROMADKA_2  ->  Prubezne procvicovani slovicek.
HROMADKA_3  ->  Prubezne procvicovani slovicek.
HROMADKA_4  ->  Prubezne procvicovani slovicek.
HROMADKA_5  ->  Zde jsou ulozena slovicka, ktera se behem behu souboru jiz neprocvicuji.
                Tato slovicka jiz uzivatel zna, ale muze je v pripade potreby smazat nebo presunout do HROMADKA_1.

Poznamka: Data v CSV jsou vzdy nahrana ve formatu: "CZ;ENG" a oddelena strednikem
napriklad: pes;dog

Cely program se provadi pres funkci menu(), ktera dle odpovedi zadane uzivatelem, presmeruje program na dalsi funkce.

'''

import csv
import sys

HROMADKA_0 = 'z.0.hromadka_spatne_odpovedi.csv'
HROMADKA_1 = 'z.1.hromadka_ENG_CZ.csv'
HROMADKA_2 = 'z.2.hromadka_CZ_ENG.csv'
HROMADKA_3 = 'z.3.hromadka_ENG_CZ.csv'
HROMADKA_4 = 'z.4.hromadka_CZ_ENG.csv'
HROMADKA_5 = 'z.5.hromadka_FINAL.csv'

DATUM = '15/10/2024'
DELIMITER = ';'


# --------------------

def uvodni_tabulka():
    '''
    Zobrazi uvodni prehled.
    Pracuje s konstantni promennou DATUM.
    Nic nevraci.
    '''
    print(f'''\nVítejte u prográmku "Hromada plná slovíček!"
autor: Samuel Raška     verze: 1.0      datum: {DATUM}
    
---------- ÚVOD ----------
-> Procvičte si dané slovíčko několikrát, což zvyšuje pravděpodobnost, že se uloží do dlouhodobé paměti.
-> Slovíčka jsou uložena do pěti hromádek, kdy každé slovíčko začíná v první hromádce. Pokud odpovíte správně,
   tak se slovíčko přesune do další hromádky, až nakonec skončí ve Finální hromádce.
-> Pokud odpovíte špatně, tak se slovíčko přesune zpět do první hromádky a celý proces začíná znovu.
-> Je možno procvičovat slovíčka, ale také celé fráze nebo věty.
-> Celý prográmek začíná procvičovat od čtvrté hromádky, aby nedocházelo k dublování slovíček.
-> Pokud v průběhu programu stisknete písmeno "Q" nebo "q", sekvence se ukončí a zobrazí se menu.''')


def napoveda():
    '''
    Zobrazi pouze napovedu.
    Nic nevraci.
    '''
    print('''\n---------- NÁPOVĚDA ----------
-> Pro rychlejší komunikaci stačí zadat ENTER místo "ne" a místo "ano" stačí napsat pouze "a".
-> Program dodržuje diakritiku, takže "královna" / "kralovna" jsou dvě různá slova
   ale je tolerantní vůči malým a velkým spísmenům, takže "pes" / "Pes" jsou pro něj stejná slova.
-> Pokud v průběhu programu stisknete písmeno "Q" nebo "q", sekvence se ukončí a zobrazí se menu.''')
    menu()


def chces_pridat_nova_slovicka(hromadka_1: str = HROMADKA_1,
                               hromadka_2: str = HROMADKA_2,
                               hromadka_3: str = HROMADKA_3,
                               hromadka_4: str = HROMADKA_4,
                               hromadka_5: str = HROMADKA_5):
    '''
    Nacte vsechny slovniky do slovnik_k_porovnani, ktery nacte do funkce zadej_nova_slovicka.
    nova_slovicka_slovnik obsahuje slovnik novych a zkontrolovcanych slovicek.
    Pote zkontroluje, jestli jsou nejaka data v nova_slovicka_slovnik.
    Pokud ano, tak je nahraje do hromadka_1, provede hlaseni a navrati se do menu()
    Pokud nejsou data ve slovniku, tak poda hlaseni a prejde navrati se do menu()

    :param hromadka_1: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_1: str
    :param hromadka_2: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_2: str
    :param hromadka_3: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_3: str
    :param hromadka_4: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_4: str
    :param hromadka_5: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_5: str
    :return: Nothing.
    '''
    slovnik_k_porovnani = {}
    slovnik_k_porovnani.update(nacist_data_do_slovniku(hromadka_1))
    slovnik_k_porovnani.update(nacist_data_do_slovniku(hromadka_2))
    slovnik_k_porovnani.update(nacist_data_do_slovniku(hromadka_3))
    slovnik_k_porovnani.update(nacist_data_do_slovniku(hromadka_4))
    slovnik_k_porovnani.update(nacist_data_do_slovniku(hromadka_5))
    # Ulozi zadana data do promenne a pri vstupu overuje, jestli uz se polozka nenachazi v databazi
    nova_slovicka_slovnik = zadej_nova_slovicka(**slovnik_k_porovnani)
    pravda_nepravda = bool(nova_slovicka_slovnik)
    if pravda_nepravda == True:
        pridej_data(hromadka_1, **nova_slovicka_slovnik)
        print('\nProvedeno! Do databáze byla nahrána tato slovíčka:')
        for key, value in nova_slovicka_slovnik.items():
            print(f'CZ: {key:<10} | ENG: {value:<10} |')
        menu()
    if pravda_nepravda == False:
        print('Nebyla nahrána žádná nová slovíčka.')
        menu()


def zadej_nova_slovicka(**kwargs: dict):
    '''
    Nacita z klavesnice ceske + anglicke slovo,
    v pripade shody s databazi oznami duplicitu a vyvola smycku od zacatku.
    Jakmile je zadany prazdny znak nebo pismena 'Q' / 'q', tak smycka konci.

    :param kwargs: Vsechna slovicka v databazi.
    :type: dict
    :return: Zadana slovicka od uzivatele, ktera prosla kontrolou.
    :rtype: dict
    '''
    nova_slovicka = {}
    print()
    while True:
        slovo_cz = input('Napište české slovo: ')
        if slovo_cz == 'Q' or slovo_cz == 'q':
            break
        if slovo_cz == '':
            break
        if kontrola_duplicity(slovo_cz, **kwargs):
            print('Toto slovo už se nachází v databázi!')
            continue
        slovo_aj = input('Napište anglické slovo: ')
        if slovo_aj == '':
            break
        nova_slovicka[slovo_cz.strip()] = slovo_aj.strip()

    return nova_slovicka


def presun_slovicka(hromadka_5: str = HROMADKA_5,
                    hromadka_1: str = HROMADKA_1):
    '''
    Presouva slovicka z Finalni hromadky do prvni dle zadaneho poctu. Slovicka odebira od zacatku souboru.
    Na zacatku overi, jestli jsou ve Finalni hromadce nejaka data, pokud ano, tak zobrazi jejich pocet.
    Pote nacita z klavesnice, kolik chce uzivatel presunout slovicek a provadi validaci vstupu.
    Pokud se zada prazdny znak, 'Q' / 'q' tak se funkce ukonci a navraci uzivatele do menu().
    Validace vstupu: Vstup nesmi byt 0, vetsi nez pocet slov v hromadce a musi se zadat pouze cislo.
    Na zaver provede presun dat a vypise uzivateli, kolik slovicek se presunulo.

    :param hromadka_5: Odkaz na konstantu - adresa CSV souboru.
    :type: str
    :param hromadka_1: Odkaz na konstantu - adresa CSV souboru.
    :type: str
    :return: Nothing.
    '''
    # Cely proces umoznuje presunou slovicka z Finalni hromadky do prvni
    pocet_s5 = ukaz_pocet_slovicek(hromadka_5)
    if pocet_s5 == 0:
        print('\nVe Finální hromádce se nenacházejí žádná slovíčka.')
        menu()

    print(f'\nPočet slovíček ve Finální hromádce: {pocet_s5}')
    pocet_k_presunu = 0
    while True:
        pocet_k_presunu = input(f'Kolik slovíček chcete přesunout? Maximálně {pocet_s5}: ')
        if pocet_k_presunu == 'Q' or pocet_k_presunu == 'q':
            menu()
            break
        if pocet_k_presunu == '':
            menu()
            break
        if not pocet_k_presunu.isdigit():
            print('Je třeba zadat číslo!')
            continue
        pocet_k_presunu = int(pocet_k_presunu)
        if pocet_k_presunu > pocet_s5:
            print(f'Počet nesmí být větší než {pocet_s5}!')
            continue
        if pocet_k_presunu == 0:
            print('Počet nesmí být nulový')
            continue
        break

    # Nacte celou hromadku a ulozi do promenne
    nacteny_slovnik = nacist_data_do_slovniku(hromadka_5)
    # Dle pocitadla vytvori dva slovniky
    slovnik_k_presunu, slovnik_puvodni = selekce_slovicek_podle_poctu(pocet_k_presunu, pocet_s5, **nacteny_slovnik)
    # slovnik_k_nahrani se zapise do puvodniho souboru (write), cimz se prepisou vsechna stavajici data
    prepis_data(hromadka_5, **slovnik_puvodni)
    # spravne_odpovedi se posunou do dalsi hromadky (append)
    pridej_data(hromadka_1, **slovnik_k_presunu)
    print(f'Provedeno! Počet přesunutých slovíček: {pocet_k_presunu}')
    menu()


def smazat_slovicka_ve_finalni_hromadce(hromadka_5: str = HROMADKA_5):
    '''
    Funkce maze slovicka ve Finalni hromadce. Probiha validace vstupnich dat od uzivatele:
    Pokud zada prazdny znak, 'Q' nebo 'q', tak se funkce ukonci a navrati uzivatele zpet do menu().
    Pokud uzivatel zada slovo, ktere uz je v databazi, oznami chybu a spusti smycku od zacatku.
    Jakmile uzivatel vymaze vsechna slovicka z nacteny_slovnik, tak se funkce ukonci.

    :param hromadka_5: Odkaz na konstantu - adresa CSV souboru.
    :type: str
    :return: Nothing.
    '''
    # Nacte celou hromadku a ulozi do promenne
    nacteny_slovnik = nacist_data_do_slovniku(hromadka_5)
    if bool(nacteny_slovnik) == False:
        print('\nVe Finální hromádce nejsou žádná slovíčka.')
        menu()

    print('''\nSlovíčka je třeba mazat jedno po druhém a zadávat české slovo.
V tomto případě program rozlišuje malá a velká písmena.
Pro ukončení sekvence zadejte ENTER:\n''')
    for key, value in nacteny_slovnik.items():
        print(f'CZ: {key:<10} | ENG: {value:<10} |')
    while True:
        rozhodnuti = input('Které slovíčko chcete smazat? -> ')
        if rozhodnuti == '':
            prepis_data(hromadka_5, **nacteny_slovnik)
            menu()
            break
        if rozhodnuti == 'Q' or rozhodnuti == 'q':
            prepis_data(hromadka_5, **nacteny_slovnik)
            menu()
            break
        if rozhodnuti not in nacteny_slovnik:
            print(f'Slovíčko "{rozhodnuti}" se nenachází v databázi!')
            continue
        nacteny_slovnik.pop(rozhodnuti)
        print(f'Provedeno! "{rozhodnuti}" vymazáno!')

        if bool(nacteny_slovnik) == False:
            print('Ve Finální hromádce už nejsou žádná slovíčka.')
            prepis_data(hromadka_5, **nacteny_slovnik)
            menu()
            break


def kontrola_duplicity(slovo: str, **kwargs: dict):
    '''
    Porovnava duplicitu zadaneho slovicka s klici v nahranem slovniku.

    :param slovo: Nove nactene slovo od uzivatele
    :type: str
    :param kwargs: Vsechna slovicka v databazi.
    :type: dict
    :return: True / False
    '''
    for key in kwargs.keys():
        if slovo.upper().strip() == key.upper():
            return True
    return False


def ukaz_pocet_slovicek(soubor: str):
    '''
    Spocita, kolik polozek se nachazi v souboru, ktery mu zadam jako parametr.

    :param soubor: Odkaz na umisteni CSV souboru.
    :type: str
    :return: Kolik polozek se nachazi v danem souboru.
    :rtype: int
    '''
    with open(soubor, 'r') as csvfile:
        slovnik = csv.reader(csvfile, delimiter=DELIMITER)
        pocitadlo_slovicek = 0
        for row in slovnik:
            if row != '':
                pocitadlo_slovicek += 1
    return pocitadlo_slovicek


def zobraz_pocty_v_hromadkach(hromadka_1: str = HROMADKA_1,
                              hromadka_2: str = HROMADKA_2,
                              hromadka_3: str = HROMADKA_3,
                              hromadka_4: str = HROMADKA_4,
                              hromadka_5: str = HROMADKA_5):
    '''
    Zobrazi uzivateli, kolik slovicek (polozek) se nachazi v databazich,
    ktere funkce nacita jako parametry.

    :param hromadka_1: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_1: str
    :param hromadka_2: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_2: str
    :param hromadka_3: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_3: str
    :param hromadka_4: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_4: str
    :param hromadka_5: Odkaz na konstantu - adresa CSV souboru.
    :type hromadka_5: str
    :return: 4x pocty polozek, ktere se nachazeji v hromadkach 1 az 4
    :rtype: int
    '''
    # Nacte pocty slovicek v databazi
    s1 = ukaz_pocet_slovicek(hromadka_1)
    s2 = ukaz_pocet_slovicek(hromadka_2)
    s3 = ukaz_pocet_slovicek(hromadka_3)
    s4 = ukaz_pocet_slovicek(hromadka_4)
    s5 = ukaz_pocet_slovicek(hromadka_5)

    # Zobrazi pocty slovicek z kazde kategorie
    nadpis = 'Počty slovíček v hromádkách:'
    delka_nadpisu = len(nadpis)
    print(f'\n{nadpis}')
    print(f'1.Hromádka{s1:.>{delka_nadpisu - 10}}')
    print(f'2.Hromádka{s2:.>{delka_nadpisu - 10}}')
    print(f'3.Hromádka{s3:.>{delka_nadpisu - 10}}')
    print(f'4.Hromádka{s4:.>{delka_nadpisu - 10}}')
    print(f'Finální hromádka{s5:.>{delka_nadpisu - 16}}\n')
    return s1, s2, s3, s4


def zadej_pocet_opakovani(*args: int):
    '''
    Uzivatelem zadane cislo porovna s nejvyssim poctem polozek z databaze. Validace vstupnich dat:
    Pokud uzivatel zada prazdny znak, 'Q' nebo 'q', tak funkce konci a vraci se do menu().
    Vstup musi byt cislo. Vstup nesmi byt nula a nesmi byt vyssi, nez nejvyssi mnozstvi z databaze.

    :param args: 4x pocty polozek, ktere se nachazeji v hromadkach 1 az 4
    :type: int
    :return: Kolik polozek chce uzivatel procvicit.
    :rtype: int
    '''
    maximalek = max(args)
    while True:
        pocet = input(f'Kolik slovíček chcete procvičit z každé hromádky? Maximálně {maximalek}: ')
        if pocet == '':
            menu()
            break
        if pocet == 'Q' or pocet == 'q':
            menu()
            break
        if not pocet.isdigit():
            print('Je třeba zadat číslo!')
            continue
        pocet = int(pocet)
        if pocet > maximalek:
            print(f'Počet nesmí být větší než {maximalek}!')
            continue
        if pocet == 0:
            print('Počet nesmí být nulový.')
            continue
        break

    return pocet


def selekce_slovicek_podle_poctu(pocet_opakovani: int, pocet_slovicek: int, **kwargs: dict):
    '''
    Roztridi slovnik na dalsi dva podle zadaneho poctu.

   :param pocet_opakovani: Kolik slovicek z jedne hromadky chce uzivatel procvicit.
   :type: int
   :param pocet_slovicek: Kolik polozek se nachazi v dane databazi.
   :type: int
   :param kwargs: Slovnik, ktery budu delit na dva.
   :type: dict
   :return: slovnik_cvicici je pripraven k procvicovani, slovnik_k_nahrani je pripraven k nahrani zpet do databaze
   :rtype: dict
    '''
    slovnik_cvicici = {}
    slovnik_k_nahrani = {}
    if pocet_opakovani == 0:
        pocet_opakovani += 1

    # Pokud chce uzivatel opakovat vicekrat, nez je polozek ve slovniku,
    # tak se pocet_opakovani snizi na maximalni pocet v databazi
    if pocet_opakovani > pocet_slovicek:
        pocet_opakovani = pocet_slovicek

    pocitadlo = pocet_opakovani - 1
    for key, value in kwargs.items():
        slovnik_cvicici[key] = value
        if pocitadlo == 0:
            break
        pocitadlo -= 1

    pocitadlo = 0
    for key, value in kwargs.items():
        pocitadlo += 1
        if pocitadlo <= pocet_opakovani:
            continue
        slovnik_k_nahrani[key] = value

    return slovnik_cvicici, slovnik_k_nahrani


def kontrola_slovicek_cz_to_eng(**kwargs: dict):
    '''
    Kontroluje, jestli uzivatelem zadana data souhlasi souhlasi s databazi.
    Pokud uzivatel zada prazdny znak, 'Q' nebo 'q', tak funkce konci a vraci se do menu().
    Validace vstupnich dat: Funkce porovnava vzdy normalizovana data (upper),
    takze funkce neni citliva na mala / velka pismena.
    Pocitaji se spravne a spatne odpovedi.

    :param kwargs: Slovnik, ktery budu kontrolovat.
    :type: dict
    :return: 2x pocitadlo uspesnosti, 1x slovicka, ktera prosla testem, 1x slovicka, ktera neprosla testem
    :rtype: int, int, dict, dict
    '''
    pocitadlo_spravne = 0
    pocitadlo_spatne = 0
    spravne_odpovedi = {}
    spatne_odpovedi = {}
    for key, value in kwargs.items():
        odpoved = input(f'Jak se "{key}" řekne anglicky? ->: ')
        if odpoved == '':
            menu()
            break
        if odpoved == 'Q' or odpoved == 'q':
            menu()
            break
        if value.upper() == odpoved.upper():
            pocitadlo_spravne += 1
            spravne_odpovedi[key] = value
            print('Správně!')
        else:
            pocitadlo_spatne += 1
            spatne_odpovedi[key] = value
            print(f'Špatně! Mělo být: "{value}"')

    return pocitadlo_spravne, pocitadlo_spatne, spravne_odpovedi, spatne_odpovedi


def kontrola_slovicek_eng_to_cz(**kwargs: dict):
    '''
    Kontroluje, jestli uzivatelem zadana data souhlasi souhlasi s databazi.
    Pokud uzivatel zada prazdny znak, 'Q' nebo 'q', tak funkce konci a vraci se do menu().
    Validace vstupnich dat: Funkce porovnava vzdy normalizovana data (upper),
    takze funkce neni citliva na mala / velka pismena.
    Pocitaji se spravne a spatne odpovedi.

    :param kwargs: Slovnik, ktery budu kontrolovat.
    :type: dict
    :return: 2x pocitadlo uspesnosti, 1x slovicka, ktera prosla testem, 1x slovicka, ktera neprosla testem
    :rtype: int, int, dict, dict
    '''
    pocitadlo_spravne = 0
    pocitadlo_spatne = 0
    spravne_odpovedi = {}
    spatne_odpovedi = {}
    for key, value in kwargs.items():
        odpoved = input(f'Jak se "{value}" řekne česky? ->: ')
        if odpoved == '':
            menu()
            break
        if odpoved == 'Q' or odpoved == 'q':
            menu()
            break
        if key.upper() == odpoved.upper():
            pocitadlo_spravne += 1
            spravne_odpovedi[key] = value
            print('Správně!')
        else:
            pocitadlo_spatne += 1
            spatne_odpovedi[key] = value
            print(f'Špatně! Mělo být: "{key}"')

    return pocitadlo_spravne, pocitadlo_spatne, spravne_odpovedi, spatne_odpovedi


def prepis_data(soubor: str, **kwargs: dict):
    '''
    Data uvedena v parametru funkce PREPISE (write) do uvedeneho souboru.

    :param soubor: Adresa CSV souboru.
    :type: str
    :param kwargs: Data, ktera budu nahravat do uvedeneho CSV souboru.
    :type: dict
    '''
    with open(soubor, 'w', encoding='utf-8', newline='') as csvfile:
        slovnik = csv.writer(csvfile, delimiter=DELIMITER)
        slovnik.writerows(kwargs.items())


def pridej_data(soubor: str, **kwargs: dict):
    '''
    Data uvedena v parametru funkce PRIDA (append) do uvedeneho souboru.

    :param soubor: Adresa CSV souboru.
    :type: str
    :param kwargs: Data, ktera budu nahravat do uvedeneho CSV souboru.
    :type: dict
    '''
    with open(soubor, 'a', encoding='utf-8', newline='') as csvfile:
        slovnik = csv.writer(csvfile, delimiter=DELIMITER)
        slovnik.writerows(kwargs.items())


def nacist_data_do_slovniku(soubor: str):
    '''
    Nacte vsechna data v souboru a ulozi do slovniku.

    :param soubor: Adresa CSV souboru.
    :type: str
    :return: Nahrana data z uvedeneho souboru.
    :rtype: dict
    '''
    with open(soubor, 'r', encoding='utf-8') as csvfile:
        slovnik = csv.reader(csvfile, delimiter=DELIMITER)
        slovicka = {}
        for row in slovnik:
            slovicka[row[0]] = row[1]
        return slovicka


def celkova_bilance(nadpis: str,
                    spravne: int = 0,
                    spatne: int = 0):
    '''
    Zobrazi pocet spravnych a spatnych odpovedi.

    :param nadpis: Jaky bude nadpis tabulky.
    :type: str
    :param spravne: Pocet spravnych odpovedi.
    :type: str
    :param spatne: Pocet spatnych odpovedi.
    :type: str
    :return: Nothing.
    '''
    delka_nadpisu = len(nadpis)
    print(f'''\n{nadpis}
Správně{spravne:.>{delka_nadpisu - 7}}
Špatně{spatne:.>{delka_nadpisu - 6}}''')


def kompletni_cviceni_slovicek(nadpis: str,
                               pocet_op: int,
                               pocet_s: int,
                               hromadka_hlavni: str,
                               hromadka_dalsi: str,
                               hromadka_0: str = HROMADKA_0,
                               cz_eng: bool = True):
    '''
    Zobrazuje a procvicuje konkretni hromadku dle zadanych dat.

    :param nadpis: Jaka hromadka se prave procvicuje.
    :type: str
    :param pocet_op: Kolik opakovani zadal uzivatel.
    :type: int
    :param pocet_s: Kolik slovicek se nachazi v dane hromadce.
    :type: int
    :param hromadka_hlavni: Odkaz na CSV soubor, ze ktereho se data budou nacitat.
    :type: str
    :param hromadka_dalsi: Odkaz na CSV soubor, kam se budou ukladat spravne odpovedi.
    :type: str
    :param hromadka_0: Odkaz na CSV soubor, kam se budou ukladat SPATNE odpovedi
    :type: str
    :param cz_eng: Argument urcuje, jestli se bude procvicovat CZ / ENG nebo obracene.
    :type: bool
    :return: spravne odpovedi, spatne odpovedi
    :rtype: dict, dict
    '''
    print(f'\n{nadpis}')
    if pocet_s != 0:
        # Nacte celou hromadku a ulozi do promenne
        nacteny_slovnik = nacist_data_do_slovniku(hromadka_hlavni)

        # Dle pocitadla vytvori dva slovniky
        slovnik_cvicici, slovnik_k_nahrani = selekce_slovicek_podle_poctu(pocet_op, pocet_s, **nacteny_slovnik)

        # Vybiram dve varianty, pokud chci cvicit anglicka nebo ceska slovicka
        # slovnik_cvicici se preda ke kontrole a podle spravnych / spatnych odpovedi se roztridi do dvou slovniku
        if cz_eng == True:
            spravne, spatne, spravne_odpovedi, spatne_odpovedi = kontrola_slovicek_cz_to_eng(**slovnik_cvicici)
        if cz_eng == False:
            spravne, spatne, spravne_odpovedi, spatne_odpovedi = kontrola_slovicek_eng_to_cz(**slovnik_cvicici)

        # slovnik_k_nahrani se zapise do puvodniho souboru (write), cimz se prepisou vsechna stavajici data
        prepis_data(hromadka_hlavni, **slovnik_k_nahrani)
        # spravne_odpovedi se posunou do dalsi hromadky (append)
        pridej_data(hromadka_dalsi, **spravne_odpovedi)
        # spatne_odpovedi se pridaji do 0.Hromadky (append)
        pridej_data(hromadka_0, **spatne_odpovedi)
    if pocet_s == 0:
        # Pokud v hromadce neni zadne slovo, tak se vypise oznameni
        # a priradi nula k odpovedim, aby program nehavaroval
        print('-> Tato hromádka je prázdná')
        spravne = 0
        spatne = 0
    return spravne, spatne


def procvicit_slovicka(hromadka_0: str = HROMADKA_0,
                       hromadka_1: str = HROMADKA_1,
                       hromadka_2: str = HROMADKA_2,
                       hromadka_3: str = HROMADKA_3,
                       hromadka_4: str = HROMADKA_4,
                       hromadka_5: str = HROMADKA_5):
    '''
    Funkce nejdrive nacte pocty polozek z jednotlivych souboru. Pote vyzve uzivatele k zadani poctu opakovani.
    Behem provadeni se nacitani spravne a spatne odpovedi (int).
    Na zaver se vse nahraje zpet do databaze a zobrazi se vysledek (viy popis konkretnich kroku).

    :param hromadka_0: Odkaz na CSV soubor, ktery obsahuje pouze spatne odpovedi.
    :type: str
    :param hromadka_1: Odkaz na CSV soubor.
    :type: str
    :param hromadka_2: Odkaz na CSV soubor.
    :type: str
    :param hromadka_3: Odkaz na CSV soubor.
    :type: str
    :param hromadka_4: Odkaz na CSV soubor.
    :type: str
    :param hromadka_5: Odkaz na CSV soubor.
    :type: str
    :return: Nothing
    '''
    nadpis_4 = '4.Hromádka = CZ -> ENG:'
    nadpis_3 = '3.Hromádka = ENG -> CZ:'
    nadpis_2 = '2.Hromádka = CZ -> ENG:'
    nadpis_1 = '1.Hromádka = ENG -> CZ:'
    nadpis_0 = 'Celková bilance odpovědí:'

    s1, s2, s3, s4 = zobraz_pocty_v_hromadkach()
    pocet_opakovani = zadej_pocet_opakovani(s1, s2, s3, s4)
    spravne4, spatne4 = kompletni_cviceni_slovicek(nadpis_4, pocet_opakovani, s4, hromadka_4, hromadka_5, cz_eng=True)
    spravne3, spatne3 = kompletni_cviceni_slovicek(nadpis_3, pocet_opakovani, s3, hromadka_3, hromadka_4, cz_eng=False)
    spravne2, spatne2 = kompletni_cviceni_slovicek(nadpis_2, pocet_opakovani, s2, hromadka_2, hromadka_3, cz_eng=True)
    spravne1, spatne1 = kompletni_cviceni_slovicek(nadpis_1, pocet_opakovani, s1, hromadka_1, hromadka_2, cz_eng=False)

    # na zaver se nahraji vsechna slovicka z 0.Hromadky na konec 1. hromadky
    slovnik_spatnych_odpovedi = nacist_data_do_slovniku(hromadka_0)
    pridej_data(hromadka_1, **slovnik_spatnych_odpovedi)
    # vycisti 0. Hromadku
    prazdny_slovnik = {}
    prepis_data(hromadka_0, **prazdny_slovnik)
    # Secte spravne a spatne odpovedi a vutiskne bilanci
    pocet_spravnych_odpovedi = spravne1 + spravne2 + spravne3 + spravne4
    pocet_spatmych_odpovedi = spatne1 + spatne2 + spatne3 + spatne4
    celkova_bilance(nadpis_0, pocet_spravnych_odpovedi, pocet_spatmych_odpovedi)
    menu()


def menu():
    '''
    Zobrazi menu, kde si uzivatel muze vybrat z jednotlivych akci.
    Validace vstupnich dat: Vstup musi byt cislo a byt v rozsahu 1 a6 6.
    Podle zadaneho cisla (odpovedi) se spusti uvedena funkce.

    :return: Nothing.
    '''
    print('''\n---------- MENU ----------
1) Procvičit slovíčka
2) Přidat nová slovíčka
3) Přesunout slovíčka z Finální hromádky do první
4) Smazat slovíčka ve Finální hromádce
5) Zobrazit nápovědu
6) Ukončit program''')
    while True:
        zadani = input('   Jakou variantu chcete provést? -> ')
        if not zadani.isdigit():
            print('Je třeba zadat číslo!')
            continue
        if zadani == '':
            print('Je třeba zadat číslo od 1 do 6')
            continue
        zadani = int(zadani)
        if zadani < 1 or zadani > 6:
            print('Je třeba zadat číslo od 1 do 6')
        if zadani == 1:
            procvicit_slovicka()
        if zadani == 2:
            chces_pridat_nova_slovicka()
        if zadani == 3:
            presun_slovicka()
        if zadani == 4:
            smazat_slovicka_ve_finalni_hromadce()
        if zadani == 5:
            napoveda()
        if zadani == 6:
            print('\n---------- Konec programu ----------')
            sys.exit()  # Okamzite ukonci program


# --------------------

# Pro jistotu vycisti 0. Hromadku
prazdny_slovnik = {}
prepis_data(HROMADKA_0, **prazdny_slovnik)

uvodni_tabulka()

menu()
