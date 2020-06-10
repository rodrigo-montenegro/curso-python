class Usuario:
    pass #sentencia nula

    def saluda(self, nombre):
        print("Hola, soy un usuario " + nombre)

codi = Usuario()  #instancia


facilito = Usuario()

print(type(codi))

codi.saluda("Codi")
facilito.saluda("Facilito")
