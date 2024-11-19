"""
Binarni cisla

        8 4 2 1
        -------
        0 0 0 0 - 0
        0 0 0 1 - 1
        0 0 1 0 - 2
        0 0 1 1 - 3
        0 1 0 0 - 4
        0 1 0 1 - 5
        0 1 1 0 - 6
        0 1 1 1 - 7
        1 0 0 0 - 8
        1 0 0 1 - 9
        1 0 1 0 - 10
        1 0 1 1 - 11
        1 1 0 0 - 12
        1 1 0 1 - 13
        1 1 1 0 - 14
        1 1 1 1 - 15

AND - 1  kdyz oba 1        &
OR - 1 kdyz nejaky je 1    |
XOR - 1 kdyz 1/0           ^
NOT - 0 kdyz 1, 1 kdyz 0   ~
"""

zprava = 'ahoj kamarade'
klic = '1'


def sifruj(sifrovany_text: str, sifrovaci_klic: str = 'x'):
    """Sifrujeme text zvolenym klicem"""
    vysledek = ''
    for znak in sifrovany_text:
        zasifrovany_znak = chr(ord(znak) ^ ord(sifrovaci_klic))
        vysledek += zasifrovany_znak

    return vysledek


print(f"puvodni zprava: {zprava}")
zasifrovana_zprava = sifruj(zprava, klic)
print(f"sifrovana zprava: {zasifrovana_zprava}")
print(f"zprava pro kamarada: {sifruj(zasifrovana_zprava, klic)}")
