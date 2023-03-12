from random import randrange
import time

#tworzenie listy z losowymi wartosciami

lista = []
i = 0
while i<1000:
    lista.append(randrange(-100,100))
    i += 1
print("Lista przed posortowaniem: ")
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

    timer_start = time.time()
    sortowanie = True
    while sortowanie:
        sortowanie = False
        for i in range(len(lista1)-1):
            if lista1[i] > lista1[i+1]:
                lista1[i], lista1[i+1] = lista1[i+1], lista1[i]
                sortowanie = True
                iteracje +=1
    timer_stop = time.time()
    print("Czas wykokania: "+str('%.2f' % ((timer_stop - timer_start)*1000))+" ms")
    print("Ilosc iteracji:"+str(iteracje))
    print("Lista po sortowaniu:")
    return str(lista1)+"\n"


#sortowanie przez wstawianie (insertion sort)
#Sortowanie przez wstawianie polega na przesuwanie w lewo liczby najmniejszej
#Zaczynamy od drugiego elementu listy i równolegle z iteracjami zwiekszamy indeks elementu
#Sprawdzamy czy element listy jest mniejszy od poprzednika
#Jezeli taka sytuacja zajdzie liczby te zamianiane sa ze soba miejscami
#Algorytm ten jest dosyc prosty a dzialajac daje wrazenie odwrocnego bubble sort
#
#zlozonosc obliczeniowa: O(n^2)
#
def sortowanie_przez_wstawianie():
    print("-----SORTOWANIE-PRZEZ-WSTAWIANIE-----")
    lista1 = lista.copy()
    iteracje = 0

    timer_start = time.time()
    for i in range(1,len(lista1)):
        for y in range(i, 0,-1):
            if lista1[y]<lista1[y-1]:
                lista1[y], lista1[y-1] = lista1[y-1], lista1[y]
                iteracje += 1
            else:
                break
    timer_stop = time.time()
    print("Czas wykokania: "+str('%.2f' % ((timer_stop - timer_start)*1000))+" ms")
    print("Ilosc iteracji:"+str(iteracje))
    print("Lista po sortowaniu:")
    return str(lista1)+"\n"



#Sortowanie przez scalanie / merge sort
#Sortowanie przez scalanie jest metodą sortowania typu "dziel i zwyciężaj"
#Na samym początku dzielimy naszą listę na części (możliwie po połowie) tak długo aż nie dojdziemy do pojedyńczych elementów
#Następnie scalamy te elementy z powrotem jednak tym razem z zachowanie kolejności od najmniejszej do największej.
#Merge sort dzieli tabclie rekurencyjnie co czyni go bardziej skomplikowanym niż tradycyjne algorytmy iteracyjne
#Jest on za to o wiele szybszy, wymaga mniej porównań
#
#zlozonosc obliczeniowa: O(n log n)
#
def sortowanie_przez_scalanie():
    print("-----SORTOWANIE-PRZEZ-SCALANIE-----")
    def merge_sort(arr,iteracje):
        if len(arr) > 1:
            iteracje += 1 
            lewa_lista = arr[:len(arr)//2]
            prawa_lista = arr[len(arr)//2:]


            merge_sort(lewa_lista,iteracje)
            merge_sort(prawa_lista,iteracje)

            lewy_indeks = 0
            prawy_indeks = 0
            index_scalania = 0
            while lewy_indeks < len(lewa_lista) and prawy_indeks < len(prawa_lista):
                iteracje += 1
                if lewa_lista[lewy_indeks] < prawa_lista[prawy_indeks]:
                    arr[index_scalania] = lewa_lista[lewy_indeks]
                    lewy_indeks += 1
                else:
                    arr[index_scalania] = prawa_lista[prawy_indeks]
                    prawy_indeks += 1
                index_scalania +=1

            while lewy_indeks < len(lewa_lista):
                iteracje += 1
                arr[index_scalania] = lewa_lista[lewy_indeks]
                lewy_indeks += 1
                index_scalania += 1

            while prawy_indeks < len(prawa_lista):
                iteracje += 1
                arr[index_scalania] = prawa_lista[prawy_indeks]
                prawy_indeks += 1
                index_scalania += 1
            return(arr,iteracje)
    list = []
    timer_start = time.time()
    lista1 = lista.copy()
    iteracje = 0
    list = merge_sort(lista1, iteracje)
    timer_stop = time.time()
    print("Czas wykokania: "+str('%.2f' % ((timer_stop - timer_start)*1000))+" ms")
    print("Ilosc iteracji / rekurencji: "+str(list[1]))
    return(list[0])


print(sortowanie_babelkowe())     
print(sortowanie_przez_wstawianie())
print(sortowanie_przez_scalanie())


