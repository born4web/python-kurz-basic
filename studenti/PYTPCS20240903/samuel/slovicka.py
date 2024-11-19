
def kolik_slovicek(s1, s2, s3, s4):
    '''Nacte pocty slovicek z kazde databaze a porovna se zadanym mnozstvim'''
    poc = int(input('Kolik slovicek chces procvicit? : '))
    print('Kontrolni tisk =', poc)
    if poc > s1 or poc > s2 or poc > s3 or poc > s4:
        print('Pocet nesmi byt vetsi nez mnostvi v hromadce!')
        kolik_slovicek(s1, s2, s3, s4)

    return poc

kolik_slovicek(5,3,2,3)