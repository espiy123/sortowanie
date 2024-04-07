import random
import time
import matplotlib.pyplot as plt
import numpy as np
import sortingMethods as srt

iloscTestow = 10
dlugosc = 1000
dolnyKres = 0
gornyKres = 10000
sorting = srt.insertionSort()


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


def vTest(tabela):
    czasy = []
    for i in range(1, dlugosc):
        listaTestowa = tabela.copy()
        listaTestowa = vTableFuncion(listaTestowa[0:i])
        time1 = time.perf_counter()
        for _ in range(iloscTestow):
            sorting(listaTestowa[0:i])
        time2 = time.perf_counter()
        czasy.append((time2 - time1) / iloscTestow)
    return czasy


def test(lista):
    czasy = []
    for i in range(1, dlugosc):
        temp = lista[0:i]
        timeStart = time.perf_counter()
        for y in range(iloscTestow):
            sorting(temp)
        timeStop = time.perf_counter()
        czasy.append((timeStop - timeStart) / iloscTestow)
    return czasy


masterTable = []
for x in range(dlugosc):
    masterTable.append(random.randint(dolnyKres, gornyKres))
ascendingTable = sorted(masterTable)
descendingTable = ascendingTable[::-1]
cTable = [1 for _ in range(dlugosc)]

malejaca = np.array(test(descendingTable))
rosnaca = np.array(test(ascendingTable))
losowa = np.array(test(masterTable))
vLista = np.array(vTest(ascendingTable))
cLista = np.array(test(cTable))

plt.plot(malejaca, label='malejący')
plt.plot(rosnaca, label='rosnący')
plt.plot(losowa, label='losowa')
plt.plot(vLista, label='v-kształtne')
plt.plot(cLista, label='stała')

plt.xticks(np.arange(0, dlugosc, step=(dlugosc // 15)))
plt.legend()
plt.show()
plt.savefig('test.png')
