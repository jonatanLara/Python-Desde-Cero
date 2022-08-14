#diccionarios siempre se identica con la clave y el valor
autores = {'libro 1':'Jonatan Lara','libro 2':'Benito juarez','libro 3':'Noe Lujan'}

#imprimir solo los valores
print(autores.values())
#imprimir solo las claves
print(autores.keys())
for autor in autores:
    print(autor)

diccionario ={'a':(1,2),'b':(3,4),'c':(5,6)}
print (diccionario)

diccionario2 = autores.copy()
print(diccionario2)
print(autores.get('libro 2'))

diccionario3 = {'libro 1':1000}

#actilizar un diccionario
autores.update(diccionario3)
print(autores)