import string
import operator

ile_dokumentow = input()
dokumenty = []
for dokumenty in range(ile_dokumentow):
dokumenty.append(input(x))

ile_zapytan = input()
zapytania = []
for i in range (ile_zapytan):
zapytania.append(input(i))
indeks_wyszukiwawczy = dict()

nr_dokumentu = 0
for i in dokumenty:
    wyczyszczenie = i
    for znak in string.punctuation:
        wyczyszczenie = wyczyszczenie.replace(znak, ' ')

    wyrazy = wyczyszczenie.lower().split()
    for wyraz in wyrazy:
        if wyraz not in indeks_wyszukiwawczy:
            indeks_wyszukiwawczy[wyraz] = dict()
        if nr_dokumentu not in indeks_wyszukiwawczy[wyraz]:
            indeks_wyszukiwawczy[wyraz][nr_dokumentu] = 1
        else:
            indeks_wyszukiwawczy[wyraz][nr_dokumentu] += 1
    nr_dokumentu += 1

for zap in zapytania:
    if zap in indeks_wyszukiwawczy:
        wynik_posredni = indeks_wyszukiwawczy[zap]
        ranking=sorted(list(wynik_posredni.items()),key=operator.itemgetter(1),reverse=True)
        wynik=[poz[0] for poz in ranking]
        print(wynik)
    else:
        print([])