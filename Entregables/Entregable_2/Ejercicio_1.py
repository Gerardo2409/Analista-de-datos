from random import randint
lista = [randint(1,10) for i in range (0,10)]
print(lista)
for i in lista:
    print(f"{i} elevado al cuadrado es {i**2} y elevado al cubo es {i**3}")
    