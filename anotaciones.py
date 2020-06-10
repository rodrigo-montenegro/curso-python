def saludo(nombre : str) -> None:  #son valores que espera recibir, no son reglas
    print("Hola " + nombre)

def suma(num1 : int, num2 : int) -> int:
    return num1 + num2

nombre = "Rodrigo"
saludo(nombre)

resultado = suma(1,9)
print(resultado)