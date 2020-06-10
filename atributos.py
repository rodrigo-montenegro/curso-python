
class Usuario:
    pass #sentencia nula

    def __init__(self, username='',correo='',nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saluda(self):
        print("Hola, soy un usuario " + self.nombre)

    def mostrar_username(self):
        print(self.username)   #self hace referencia al objeto en ejecucion
    
    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self, nombre):
        self.nombre = nombre

codi = Usuario()  #instancia
codi.username = "codi"
codi.correo = "codi@gmail.com"


facilito = Usuario()
facilito.username = "facilito"
facilito.correo = "facilito@gmail.com"

codi.mostrar_username()
facilito.mostrar_username()


codi.crear_nombre("Codigo")
codi.mostrar_nombre()

rodrigo = Usuario("rod90","ro@gmail.com","Rodrigo")

resultado = rodrigo.saluda()
print(resultado)