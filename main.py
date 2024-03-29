import random
import time
import numpy as np
import matplotlib.pyplot as plt

iloscTestow = 5
dlugosc = 200
dolnyKres = 0
gornyKres = 2000
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


def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2] if n else None


def test(tabela):
    czasyWykoania = []
    sumaDlaKroku = []
    for j in range(0, iloscTestow):
        timeStart = time.perf_counter()
        for i in range(dlugosc):
            temp = 0
            temp_list = []
            for n in range(iloscTestow):
                tempTable = []
                for x in range(i):
                    tempTable.append(tabela[x])

                # timeStart = time.perf_counter()
                ###ALGORYTM###
                tempTable.sort()
                ##############
                timeStop = time.perf_counter()
                temp_list.append(timeStop - timeStart)
            if j == 0:
                sumaDlaKroku.append(timeStop - timeStart)
                czasyWykoania.append(sumaDlaKroku[i] / (j + 1))
            else:
                sumaDlaKroku[i] += (timeStop - timeStart)
                czasyWykoania[i] = sumaDlaKroku[i] / (j + 1)
    return czasyWykoania

masterTable = []
for x in range(dlugosc):
    masterTable.append(random.randint(dolnyKres, gornyKres))

ascendingTable = sorted(masterTable)
descendingTable = ascendingTable[::-1]
vTable = vTableFuncion(ascendingTable)
cTable = list(range(100))

print(cTable)

testowatablica = test(masterTable)
points = np.array(testowatablica)

plt.plot(points)
plt.show()
