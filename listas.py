#Listas se diferencian por [] estas pueden recibir cualquier datos y modificarlos
lista = [1,2,3,4,5]
lista2 = ["aaaa","bbbb","cccc"]
listas3 = [1,"c",True,1.9]
#lista[0] = 1000
for elemeto in lista:
    print(elemeto)
#agregamos un valor a la lista
lista.append(100)
print(lista)
# modificar el valor de una lista
lista[5] = 'Hola'
print(lista)
#elimna el ultimo elemento de la lista por default porque puedo decirle que posicion elimine
lista.pop()
print(lista)

listaB = [10,100,1000]
#agrega una lista con otra lista
lista.extend(listaB)
print(lista)

#borrar elementos de la lista
del lista[5]
print(lista)
# otra forma de eliminar remove(posicion)
lista.remove(2)
print(lista)

listaC = [1,2,3,4,5,6,5,5]
listaC.count(5)
print(listaC)

listaC.sort()
print(listaC)

listaC.sort(reverse=True)
print(listaC)