import string
ile_dokumentow = 3
dokumenty= []
dokumenty.append("Your care set up, do not pluck my cARe down")
dokumenty.append("Tralalala")
dokumenty.append("Your CARE is gain of Care when new care iS won.")
ile_zapytan = 2
zapytania = []
zapytania.append('care')
zapytania.append('is')
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
        print(indeks_wyszukiwawczy[zap])
    else:
        print([])
        

