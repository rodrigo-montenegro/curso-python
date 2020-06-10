#a, b , c
#a(b) -> c

def decorador(funcion): #a
       
  def nueva_funcion():
      print("Podemos agregar codigo antes")
      funcion()
      print("Podemos agregar codigo despues")  
      return nueva_funcion 


@decorador
def funcion_a_decorar():  #b
    print("Esta es una funcion a decorar")

funcion_a_decorar()