import json
with open('archivo.json') as file:
    dato = json.load(file)
print(dato)
print(dato['nombres'])
print(dato['nombres'][0])
print(dato['nombres'][0]['apellido'])