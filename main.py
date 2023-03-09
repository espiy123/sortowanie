from random import randrange

#tworzenie listy z losowymi wartosciami
def tworzenie_listy():
    lista = []
    i = 0
    while i<100:
        lista.append(randrange(0,100))
        i += 1
    print("Lista przed sortowaniem:")
    print(lista)
    return lista


#sortowanie bablekowe
#Sortowanie babelkowe listy polega na porowaniu jej elmentu z nastepnym wystepujacym elementem.
#Dowolnej zmiennej przypisujemy wartosc true aby moc zainicjowac petle while.
#Nastepnie przypisujemy jej wartosc false. Dlaczego? Zauwaz ze zaczynamy porownywac ze soba wartosci z listy.
#W przypadku gdy element listy faktycznie jest wiekszy od jego nastepcy nastepuje zamania tych wartosci miejscami a
#zmienna sortowanie ponowanie ma przypisana wartosct true aby moc wykonac kolejny krok. W przeciwsnym razie
# (gdy nie ma juz liczby, ktorej nastepca jest od niej mniejszy tzn. lista jest posortowana) warunek
# if lista[i] > lista[i+1] sie nie wykona. W takim razie petla while zostaje przerwana (zmienna sortowanie ma wartosc false)

def sortowanie_babelkowe():
    lista = tworzenie_listy()
    sortowanie = True
    while sortowanie:
        sortowanie = False
        for j in range(len(lista)):
            for i in range(len(lista)-1):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    sortowanie = True
    print("Lista po sortowaniu:")
    return lista


print(sortowanie_babelkowe())