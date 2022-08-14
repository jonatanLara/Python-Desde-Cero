#encontremos la segunda calificacion más baja

calificaciones = [["Jonatan",9],["Juan",6],["Pedro",8],["Zule",7],["Leo",10]]
''' solo funciona si no hay calificaciones repetidas
ordenar = sorted(calificaciones,key=lambda x:x[1])
print(ordenar[1][0]'''
ordenar = [x[1] for x in calificaciones]
print(ordenar)
#creamos una lista
l3 = set(ordenar)
print(l3)
l4 = list(l3)
print(l4)
l5 = sorted(l4)
print(l5)
#optenemos la calificacion mas baja
segunda = l5[1]
print(segunda)
f = filter(lambda x:x[1] == segunda,calificaciones)
print(f)
l6=list(f)
print(l6)
for x in l6:
    print(x[0])

    