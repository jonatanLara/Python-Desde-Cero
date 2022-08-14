a = 1
a = 'Hola'
a = "Hola"
a = '10'
a1 = '5'
a2 = 'jose'
print(a)
print ('Tengo {} y quiero {} manzanas me llamo {}'.format(a,a1,a2))
#print(int(a)) // cast o forzamos a que te devuelva numeros enteros
#funciones, dar pistas recibe y devuelve
#def metodo(a:int) -> int:
x = True
y = False

#comentarios
'''x = True
y = False'''

#recibir valores desde el teclado
datoA = int(input('Ingresa un número:'))
datoB = int(input('Ingresa otro número:'))
# : lo que sigue es un bloque
if(datoA>datoB):
    print('El mayor es: ',datoA)
else:
    print('El mayor es: ',datoB)
#print(datoA, datoB)

palabras = "jose"
for letras in palabras:
    print(letras)
for i in range(0,50,2):
    print (i)
