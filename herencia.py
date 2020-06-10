class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

class Perro(Animal):      #Herencia
    def __init__(self,nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

class Gato(Animal):
    def ronroneo(self):
        print("Ronroneo")


firulais = Perro("Firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()
