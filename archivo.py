def crear_archivo():
    archivo = open('data.txt','w')
    archivo.close()
def escribir_archivo():
    archivo = open('data.txt','a')
    archivo.write('Jonatan Lara\n')
    archivo.write('981106323\n')
    archivo.write('Campeche\n')
def leer_archivo():
    archivo = open('data.txt','r')
    linea = archivo.readline()
    while linea != "":
        print(linea)
        linea = archivo.readline()
    archivo.close()

crear_archivo()
escribir_archivo()
leer_archivo()