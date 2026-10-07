liczby = input("Podaj 5 liczb do listy = ").split(' ')

i = 0
while i < len(liczby):
    liczby[i] = int(liczby[i])
    i += 1


def suma(liczby: list[int]) -> int:
    wynik = 0
    i = 0

    while i < len(liczby):
        wynik += liczby[i]
        i += 1

    return wynik


def najwieksza(liczby: list[int]) -> int:
    if len(liczby) > 0:
        moja_naj = liczby[0]
        i = 1

        while i < len(liczby):
            if liczby[i] > moja_naj:
                moja_naj = liczby[i]
            i += 1

        return moja_naj
    else:
        return "puste"


def najmniejsza(liczby: list[int]) -> int:
    if len(liczby) > 0:
        moja_naj = liczby[0]
        i = 1

        while i < len(liczby):
            if liczby[i] < moja_naj:
                moja_naj = liczby[i]
            i += 1

        return moja_naj
    else:
        return "puste"


def srednia(liczby: list[int]) -> float:
    wynik = suma(liczby) / len(liczby)
    return wynik


def ile_parzystych(liczby: list[int]) -> int:
    parzyste = 0
    i = 0

    while i < len(liczby):
        if liczby[i] % 2 == 0:
            parzyste += 1
        i += 1

    return parzyste


def dupicates(liczby: list[int]) -> list[int]:
    duplikaty = []
    mozliwe = []
    i = 0

    while i < len(liczby):
        if liczby[i] in mozliwe:
            duplikaty.append(liczby[i])
        else:
            mozliwe.append(liczby[i])
        i += 1

    return duplikaty


def usuwanie_duplikatow(liczby: list[int]) -> list[int]:
    duplikaty = dupicates(liczby)
    i = 0

    while i < len(duplikaty):
        liczby.remove(duplikaty[i])
        i += 1

    return liczby


def squares(liczby: list[int]) -> list[int]:
    kwadraty = []
    i = 0

    while i < len(liczby):
        kwadraty.append(liczby[i] ** 2)
        i += 1

    return kwadraty


print(f"suma liczb z listy = {suma(liczby)}")
print(f"najwieksza liczba z listy = {najwieksza(liczby)}")
print(f"najmniejsza liczba z listy = {najmniejsza(liczby)}")
print(f"średnia liczb z listy = {srednia(liczby)}")
print(f"parzyste liczby z listy = {ile_parzystych(liczby)}")
print(f"powtarzające się liczby z listy = {dupicates(liczby)}")
print(f"kwadraty liczb z listy = {squares(liczby)}")
print(f"lista bez duplikatów = {usuwanie_duplikatow(liczby)}")