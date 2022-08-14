#las clases tiene atributos y metodos
class Persona:
    nombre =""
    edad = 0
    peso = 0
    #los metodos comunmente son verbos y teminan en infinitivo
    # contructor es la ultima oportunidad que tenemos para modificar la salida
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    # el atributo es igual a propiedad / self hace referencia yo mismo
    # las funciones y los metodos se diferencias e que una funcion devuelve algo y un metodo NO
    def saludar(self):
        print("Hola mi nombre es",self.nombre)
    def despedir(self):
        print("Hasta pronto")

pepito = Persona("jonatan",27,80.0)
print(pepito.edad)
pepito.saludar()
print(pepito.nombre,pepito.edad,pepito.peso)