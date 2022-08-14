# este formato se utiliza mucho para el almacenamiento de datos sin usar base de datos
import csv
lista = [['Jonatan',9811382181],['Pedro',9811382183],['Juan',9811384181]]

doc_csv = open("archivo.csv","w")
csv_data = csv.writer(doc_csv)

#csv_data.writerow(lista)
for elemento in lista:
    csv_data.writerow(elemento)
    print(elemento)
doc_csv.close()

doc = open("archivo.csv","r")
documento = csv.reader(doc)
for (nombre,numero) in documento:
    print(nombre,numero)
doc.close()
'''
with open("archivo.csv","r") as doc:
    documento = csv.reader(doc)
    for nombre, numero in documento:
        print(nombre, numero)'''