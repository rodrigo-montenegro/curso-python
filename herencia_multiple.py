class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

    def comun(self):
        print("Este es un metodo de Animal")

class Mascota:
    def fecha_adopcion(self,fecha):
        self.fecha_adopcion = fecha


class Perro(Animal, Mascota):      #Herencia multiple
    def __init__(self,nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

    """
    def comun(self):
        print("Este es un metodo de perro")
    """
class Gato(Animal):
    def ronroneo(self):
        print("Ronroneo")

firulais = Perro("Firulais")
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_adopcion)

firulais.comun()