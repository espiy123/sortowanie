from random import randrange

#tworzenie listy z losowymi wartosciami

lista = []
i = 0
while i<100:
    lista.append(randrange(0,100))
    i += 1
print("Lista przed sortowaniem: ")
print(str(lista)+"\n")



#sortowanie bablekowe (bubble sort)
#Sortowanie babelkowe listy polega na porowaniu jej elmentu z nastepnym wystepujacym elementem.
#Dowolnej zmiennej przypisujemy wartosc true aby moc zainicjowac petle while.
#Nastepnie przypisujemy jej wartosc false. Dlaczego? Zauwaz ze zaczynamy porownywac ze soba wartosci z listy.
#W przypadku gdy element listy faktycznie jest wiekszy od jego nastepcy nastepuje zamania tych wartosci miejscami a
#zmienna sortowanie ponowanie ma przypisana wartosct true aby moc wykonac kolejny krok. W przeciwsnym razie
# (gdy nie ma juz liczby, ktorej nastepca jest od niej mniejszy tzn. lista jest posortowana) warunek
# if lista[i] > lista[i+1] sie nie wykona. W takim wypadku petla while zostaje przerwana (zmienna sortowanie ma wartosc false)
#
#zlozonosc obliczeniowa: O(n^2)
#

def sortowanie_babelkowe():
    print("-----SORTOWANIE-BABELKOWE-----")
    lista1 = lista.copy()

    iteracje = 0
    sortowanie = True
    while sortowanie:
        sortowanie = False
        for i in range(len(lista1)-1):
            if lista1[i] > lista1[i+1]:
                lista1[i], lista1[i+1] = lista1[i+1], lista1[i]
                sortowanie = True
                iteracje +=1
    print("Ilosc iteracji:"+str(iteracje))
    print("Lista po sortowaniu:")
    return str(lista1)+"\n"


#sortowanie przez wstawianie (insertion sort)
#Sortowanie przez wstawianie polega na przesuwanie w lewo liczby najmniejszej
#Zaczynamy od drugiego elementu listy i równolegle z iteracjami zwiekszamy indeks elementu
#Sprawdzamy czy element listy jest mniejszy od poprzednika
#Jezeli taka sytuacja zajdzie liczby te zamianiane sa ze soba miejscami
#Algorytm ten jest dosyc prosty a swoim dzialaniem przypomina sortowanie babelkowe
#
#zlozonosc obliczeniowa: O(n^2)
#
def sortowanie_przez_wstawianie():
    print("-----SORTOWANIE-PRZEZ-WSTAWIANIE-----")
    lista1 = lista.copy()

    iteracje = 0
    for i in range(1,len(lista1)):
        for y in range(i, 0,-1):
            if lista1[y]<lista1[y-1]:
                lista1[y], lista1[y-1] = lista1[y-1], lista1[y]
                iteracje += 1
            else:
                break
    print("Ilosc iteracji:"+str(iteracje))
    print("Lista po sortowaniu:")
    return str(lista1)+"\n"



print(sortowanie_babelkowe())
print(sortowanie_przez_wstawianie())

