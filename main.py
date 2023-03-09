from random import randrange

#tworzenie listy z losowymi wartościami
lista = []
i = 0
while i<100:
    lista.append(randrange(0,100))
    i += 1

print(lista)