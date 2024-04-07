import random
import time
import numpy as np
import matplotlib.pyplot as plt

iloscTestow = 10
dlugosc = 500
dolnyKres = 0
gornyKres = 200
iloscSkokow = 2

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
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

# def median(lst):
#     n = len(lst)
#     s = sorted(lst)
#     return (s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2] if n else None

def vTest(tabela):
    czasy = []
    for i in range(1, dlugosc):
        listaTestowa = tabela.copy()
        listaTestowa = vTableFuncion(listaTestowa[0:i])
        time1 = time.perf_counter()
        for _ in range(iloscTestow):
            insertionSort(listaTestowa[0:i])
        time2 = time.perf_counter()
        czasy.append((time2 - time1) / iloscTestow)
    return czasy
def test(tabela):
    czasy = []
    for i in range(1, dlugosc):
        listaTestowa = tabela.copy()
        time1 = time.perf_counter()
        for _ in range(iloscTestow):
            insertionSort(listaTestowa[0:i])
        time2 = time.perf_counter()
        czasy.append((time2-time1)/iloscTestow)
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

plt.xticks(np.arange(0, dlugosc, step=(dlugosc//15)))
plt.legend()

plt.show()
plt.savefig('test.png')
