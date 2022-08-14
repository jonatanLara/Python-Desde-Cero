# tuplas pueden recibir varios tipos de datos pero no pueden modificarse o cambiar de valor
tupla = (1,2,3)
tupla2 = ('aaaa','bbbb','cccc')
tupla3 = (1,'aaaa',True,1.9)
usuario =('jonatan','jonatan2332',27,'Campeche')
print(tupla)
print(tupla2)
print(tupla3)
print(tupla3[0])

for elemento in usuario:
    print(elemento)

#tupla3[3] = 1 error tuple object dos not sopport item assi

def enviar_datos():
    nombre = 'jonatan'
    correo = 'jonatan2332'
    edad = 27
    ciudad = 'Campeche'
    #para que un funcion regrese una tupla
    return (nombre,correo,edad,ciudad)

def recibir_datos(datos):
    print(datos[0])
    print(datos[1])
    print(datos[2])

datos = enviar_datos()
recibir_datos(datos)
#una funcion puede recibir otra funcion
recibir_datos(enviar_datos())