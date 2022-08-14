import csv
lista=[]
placas=[]
frecuencias=[]
i = 0
def frecuencia_placas(placa):
    global cont; cont=0
    for fila in lista:
        cont+=fila.count(placa)
    return cont

with open("paquiadero.csv") as file:
    entrada = csv.reader(file, delimiter =';')
    # captura los datos en una lista lista :[['GVR 557', '1/3/2022', '00:23:03', 'E'], ['TPD 712', '1/3/2022', '00:34:41', 'E'],...etc
    lista = list(entrada)

for fila in lista:
    print(fila) #['GVR 557', '1/3/2022', '00:23:03', 'E']
    if fila[0] not in placas: #si la fila [en la posicion] no esta en placas
        placas.append(fila[0]) #lo agregamos a las placas
        frecuencias.insert(i,fila[0]+' '+str((frecuencia_placas(fila[0])))) #list.insert(pos, elmnt)

for placa in frecuencias:
    print(placa)

print('total de regs '+str(len(lista)))
print('total de autos regristrados '+str(len(placas)))
