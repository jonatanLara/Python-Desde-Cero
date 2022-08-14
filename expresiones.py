import re
#El siguiente patrón coincide con una cadena literal bl seguida de uno o más caracteres de palabra especificados por la \w+regla:
s = "black, blue and brown"
#cadena = "T6_12341s,T5_1421723,T6_12341s,T5_14217sdf,T6_123411231,T5_14217213,T6_12341,T5_14217"
#pattern = r'bl\w+'
#patter2 = r'T\w+'
#matches = re.findall(patter2,cadena)
#[1,8] asi le estpy diciendo que
#print(matches)
#print(matches[1])
'''Necesito recorre matches que  es una nueva lista para ver cuantos elentos se repiten en ella
per antes debo acordar a 8 digitos cada elemento de la lista 
despues crear una lista nueva donde estaran los elemento que no se repitan y contengan los 8 digitos'''
'''resultantList = []

for element in matches:
    digitos = element[0:8]
    if digitos not in resultantList:
        resultantList.append(digitos)
        print(digitos)
print(resultantList)'''

def limparDatos(Cadena):
    expresion = r'T\w+'
    matches = re.findall(expresion, Cadena)
    resultantList = []
    for element in matches:
        digitos = element[0:8]
        if digitos not in resultantList:
            resultantList.append(digitos)
    return str(resultantList)


cadena = "T6_12341s,T5_1421723,T6_12341s,T5_14217sdf,T6_123411231,T5_14217213,T6_12341,T5_14217"
#print(','.join(limparDatos(cadena)))
print (limparDatos(cadena))


