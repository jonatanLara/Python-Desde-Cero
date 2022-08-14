# hay dos tipos de herencia, herencia simple y herencia multiple
class Persona:
    nombre =""
    edad = 0
    peso = 0

    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def saludar(self):
        print("Hola mi nombre es",self.nombre)
    def despedir(self):
        print("Hasta pronto")
    #un metodo puede llamar a otro metodo siempre y cuando esten en la misma clase
    def comprar(self):
        self.saludar()
        print("Puedo comprar x cosa")
#herencia
class Empleado:
    trabajo =""
class Estudiante(Persona,Empleado):#herencia multiple
#class Estudiante(Persona): herencia simple
    escuela = ""
estudiante = Estudiante("Jonatan",27,80.0)
print(estudiante.nombre,estudiante.edad,estudiante.peso)
estudiante.saludar()
estudiante.despedir()