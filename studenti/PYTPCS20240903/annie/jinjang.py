otazky_k_pomeru_tepla = [
    "Míváš za normálních podmínek teplé ruce a teplé nohy? Odpověz 'ano', 'ne', 'nevím': ",
    "Máš horké léto raději než studenou zimu? Odpověz 'ano', 'ne', 'nevím': ",
    "Máš studenou zimu raději než horké léto? Odpověz 'ano', 'ne', 'nevím': ",
    "Míváš běžně studené ruce a studené nohy? Odpověz 'ano', 'ne', 'nevím': "
]

otazky_k_pomeru_vlhkosti = [
    "Kolik vážíš? Napiš číslo: ",
    "Kolik měříš? Napiš číslo: ",
]

otazky_k_temperamentu_1 = [
    "Cítíš se běžně plný/á energie? Odpověz 'ano', 'ne', 'nevím': ",
    "Cítíš se zřídkakdy unavený/á? Odpověz 'ano', 'ne', 'nevím': ",
    "Cítíš se normálně líně, ale nejsi unavený/á? Odpověz 'ano', 'ne', 'nevím': ",
    "Cítíš se běžně unavený/á? Odpověz 'ano', 'ne', 'nevím': "
]

otazky_k_temperamentu_2 = [
    "Neusneš nikdy jako spolujezdec v dopravním prostředku?(Usneš jen při extrémní únavě?) "
    "Odpověz 'ano', 'ne', 'nevím': ",
    "Usneš jako spolujezdec v dopravním prostředku, když jsi trochu unavený/á? "
    "Odpověz 'ano', 'ne', 'nevím': ",
    "Usneš jako spolujezdec v dopravním prostředku, dokonce i když nejsi unavený/á? "
    "Odpověz 'ano', 'ne', 'nevím': ",
    "Usneš snadno jako spolujezdec v dopravním prostředku? "
    "Odpověz 'ano', 'ne', 'nevím': "
]

otazka_k_sexualnimu_zivotu = ["Těší tě sex víc než jídlo? Odpověz 'ano', 'ne', 'nevím': "]

print("---------------")


class Vysledky:
    def __init__(self, otazky_teplo, otazky_vlhkost, otazky_temperament_1, otazky_temperament_2, otazka_sexualni_zivot):
        self.otazky_teplo = otazky_teplo
        self.otazky_vlhkost = otazky_vlhkost
        self.otazky_temperament_1 = otazky_temperament_1
        self.otazky_temperament_2 = otazky_temperament_2
        self.otazka_sexualni_zivot = otazka_sexualni_zivot

    def odpoved_pomer_tepla(self, otazka_1, otazka_2, otazka_3, otazka_4):
        mozne_odpovedi = ["ano", "ne", "nevím"]

        def odpovedi_na_otazky(otazka):

            odpoved = input(otazka)
            while odpoved not in mozne_odpovedi:
                odpoved = input(f"Nenapsal jsi platnou odpověď. Zkus to, prosím, znovu.\n{otazka}")
            return odpoved

        odpoved_1 = odpovedi_na_otazky(otazka_1)
        odpoved_2 = odpovedi_na_otazky(otazka_2)
        odpoved_3 = odpovedi_na_otazky(otazka_3)
        odpoved_4 = odpovedi_na_otazky(otazka_4)

        vysledek = 0
        if odpoved_1 == "ano":
            vysledek += 8
        if odpoved_2 == "ano":
            vysledek += 4
        if odpoved_3 == "ano":
            vysledek -= 4
        if odpoved_4 == "ano":
            vysledek -= 8

        return int(vysledek / 2) if vysledek != 0 else vysledek

    def odpoved_pomer_vlhkosti(self, otazka_1, otazka_2):

        def odpovedi_na_otazky(otazka):
            while True:
                odpoved = input(otazka)
                try:
                    odpoved = int(odpoved)
                    return odpoved
                except ValueError:
                    print(f"Nenapsal jsi platnou odpověď. Zkus to, prosím, znovu.")

        odpoved_vaha = int(odpovedi_na_otazky(otazka_1))
        odpoved_vyska = int(odpovedi_na_otazky(otazka_2))

        presna_vaha = odpoved_vyska - 100
        minimalni_optimalni_vaha = presna_vaha - 5
        maximalni_optimalni_vaha = presna_vaha + 5

        if minimalni_optimalni_vaha <= odpoved_vaha <= maximalni_optimalni_vaha:
            return 0
        else:
            nadvaha = odpoved_vaha - maximalni_optimalni_vaha

            if 1 <= nadvaha <= 2:
                return 1
            elif 3 <= nadvaha <= 5:
                return 2
            elif 6 <= nadvaha <= 8:
                return 3
            elif 9 <= nadvaha <= 11:
                return 4
            elif 12 <= nadvaha <= 14:
                return 5
            elif 15 <= nadvaha <= 17:
                return 6
            elif 18 <= nadvaha <= 20:
                return 7
            elif nadvaha > 20:
                return 8

            podvaha = minimalni_optimalni_vaha - odpoved_vaha

            if 1 <= podvaha <= 2:
                return -1
            elif 3 <= podvaha <= 5:
                return -2
            elif 6 <= podvaha <= 8:
                return -3
            elif 9 <= podvaha <= 11:
                return -4
            elif 12 <= podvaha <= 14:
                return -5
            elif 15 <= podvaha <= 17:
                return -6
            elif 18 <= podvaha <= 20:
                return -7
            elif podvaha > 20:
                return -8

    def odpoved_temperament_1(self, otazka_1, otazka_2, otazka_3, otazka_4):
        mozne_odpovedi = ["ano", "ne", "nevím"]
        odpovedi = []

        def odpovedi_na_otazky(otazka):

            odpoved = input(otazka)
            while odpoved not in mozne_odpovedi:
                odpoved = input(f"Nenapsal jsi platnou odpověď. Zkus to, prosím, znovu.\n{otazka}")
            return odpoved

        odpovedi.append(odpovedi_na_otazky(otazka_1))
        odpovedi.append(odpovedi_na_otazky(otazka_2))
        odpovedi.append(odpovedi_na_otazky(otazka_3))
        odpovedi.append(odpovedi_na_otazky(otazka_4))

        vysledek = 0
        if odpovedi == ["ano", "ne", "ne", "ne"] or odpovedi == ["ano", "ano", "ne", "ne"]:
            vysledek += 8
        elif odpovedi == ["ne", "ne", "ne", "ano"] or odpovedi == ["ne", "ne", "ano", "ano"]:
            vysledek -= 8
        else:
            if odpovedi[0] == "ano":
                vysledek += 8
            if odpovedi[1] == "ano":
                vysledek += 4
            if odpovedi[2] == "ano":
                vysledek -= 4
            if odpovedi[3] == "ano":
                vysledek -= 8

        pocet_ano = odpovedi.count("ano")
        return int(vysledek / 3) if pocet_ano == 3 else vysledek

    def odpoved_temperament_2(self, otazka_1, otazka_2, otazka_3, otazka_4):
        mozne_odpovedi = ["ano", "ne", "nevím"]
        odpovedi = []

        def odpovedi_na_otazky(otazka):

            odpoved = input(otazka)
            while odpoved not in mozne_odpovedi:
                odpoved = input(f"Nenapsal jsi platnou odpověď. Zkus to, prosím, znovu.\n{otazka}")
            return odpoved

        odpovedi.append(odpovedi_na_otazky(otazka_1))
        odpovedi.append(odpovedi_na_otazky(otazka_2))
        odpovedi.append(odpovedi_na_otazky(otazka_3))
        odpovedi.append(odpovedi_na_otazky(otazka_4))

        vysledek = 0
        if odpovedi == ["ano", "ne", "ne", "ne"] or odpovedi == ["ano", "ano", "ne", "ne"]:
            vysledek += 8
        elif odpovedi == ["ne", "ne", "ne", "ano"] or odpovedi == ["ne", "ne", "ano", "ano"]:
            vysledek -= 8
        else:
            if odpovedi[0] == "ano":
                vysledek += 8
            if odpovedi[1] == "ano":
                vysledek += 4
            if odpovedi[2] == "ano":
                vysledek -= 4
            if odpovedi[3] == "ano":
                vysledek -= 8

        pocet_ano = odpovedi.count("ano")
        return int(vysledek / 3) if pocet_ano == 3 else vysledek

    def odpoved_sexualni_zivot(self, otazka):
        mozne_odpovedi = ["ano", "ne", "nevím"]
        odpoved = input(otazka)

        while odpoved not in mozne_odpovedi:
            odpoved = input(f"Neplatná odpověď, zkus to znovu. {otazka}")

        if odpoved == "ano":
            return 4
        elif odpoved == "ne":
            return -4
        elif odpoved == "nevím":
            return 0

    def vypocet_telesneho_typu(self, teplo, vlhkost, energie, unava, sex):

        soucet = teplo + vlhkost + energie + unava + sex
        konecny_vypocet = int(round(soucet / 5))

        if konecny_vypocet == 0:
            return ("Poměr jinu a jangu je u tebe úplně vyvážený.\n"
                    "Můžeš jíst 'jinové' i 'jangové' potraviny ve stejném poměru.")
        elif konecny_vypocet < 0:
            return f"Tvůj jin-jangový poměr je {konecny_vypocet}.\nJsi jinová osoba."
        else:
            return f"Tvůj jin-jangový poměr je +{konecny_vypocet}.\nJsi jangová osoba."


vysledky = Vysledky(otazky_k_pomeru_tepla, otazky_k_pomeru_vlhkosti,
                    otazky_k_temperamentu_1, otazky_k_temperamentu_2,
                    otazka_k_sexualnimu_zivotu)

prvni_vysledek = vysledky.odpoved_pomer_tepla(*otazky_k_pomeru_tepla)
druhy_vysledek = vysledky.odpoved_pomer_vlhkosti(*otazky_k_pomeru_vlhkosti)
treti_vysledek = vysledky.odpoved_temperament_1(*otazky_k_temperamentu_1)
ctvrty_vysledek = vysledky.odpoved_temperament_2(*otazky_k_temperamentu_2)
paty_vysledek = vysledky.odpoved_sexualni_zivot(*otazka_k_sexualnimu_zivotu)
konecny_vysledek = vysledky.vypocet_telesneho_typu(prvni_vysledek, druhy_vysledek,
                                                   treti_vysledek, ctvrty_vysledek, paty_vysledek)

print()
print(konecny_vysledek)
print()
print(f"HODNOCENÍ PODROBNĚJI:\nTvůj jin-jangový poměr tepla je {prvni_vysledek}.\n"
      f"Tvůj jin-jangový poměr vlhkosti je {druhy_vysledek}.\nStav tvojí tělesné energie odpovídá jin-jangovému poměru {treti_vysledek}.\n"
      f"Tvoje energetické dispozice odpovídají jin-jangovému poměru {ctvrty_vysledek}.\n"
      f"Tvůj sexuální život odpovídá jin-jangovému poměru {paty_vysledek}.")
