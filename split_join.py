lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScriot; C#; C; C++" 

separador = "; "
lista_generada = lenguajes.split(separador)

nuevo_string = "_".join(lista_generada)

texto = """ Este es un texto 
con
saltos
de 

linea

"""

resultado = texto.splitlines()

print(lista_generada)
print(nuevo_string)
print(resultado)