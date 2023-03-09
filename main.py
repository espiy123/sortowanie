from random import randrange

#tworzenie listy z losowymi wartosciami
lista = []
i = 0
while i<100:
    lista.append(randrange(0,100))
    i += 1

#sortowanie bablekowe
def sortowanie_babelkowe():
    for j in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            else:
                continue
    return lista

print(sortowanie_babelkowe())