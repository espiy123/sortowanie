import random
import time
import csv
import sortingMethods as srt

iloscTestow = 20
dolnyKres = 0
gornyKres = 30000
sorting = srt.heapSort


def vTableFuncion(table):
    table1 = []
    table2 = []
    for i in range(len(table)):
        if i % 2 == 1:
            table1.append(table[i])
        else:
            table2.append(table[i])
    table1 = table1[::-1]
    vShape = table1 + table2
    return vShape
def test(lista):
    startTime = time.perf_counter()
    for i in range(iloscTestow):
        sorting(lista)
    stopTime = time.perf_counter()
    return (stopTime-startTime)/iloscTestow


wynikiAscending = []

wynikiDescending = []

wynikiCTable = []

wynikiVTable = []

wynikiRandom = []

indeksy = []
naglowki = ['Rosnacy', "Malejacy", "Staly", "V-kształtny", "Losowy"]
for x in range(2000,30001,2000):
    lista = []
    for _ in range(x):
        lista.append(random.randint(dolnyKres,gornyKres))


    ascending = sorted(lista)
    descending = ascending[::-1]
    cTable = [1 for _ in range(x)]
    vTable = vTableFuncion(ascending)

    wynikiRandom.append(test(lista))
    wynikiAscending.append(test(ascending))
    wynikiDescending.append(test(descending))
    wynikiCTable.append(test(cTable))
    wynikiVTable.append(test(vTable))

    indeksy.append(x)

with open("wyniki.csv", mode='w', newline='') as plik_csv:
    writer = csv.writer(plik_csv)
    writer.writerow(['Rozmiar'] + naglowki)
    for indeks, asc, desc, ctable, vtable, rand in zip(indeksy, wynikiAscending, wynikiDescending, wynikiCTable, wynikiVTable, wynikiRandom):
        writer.writerow([indeks, asc, desc, ctable, vtable, rand])


