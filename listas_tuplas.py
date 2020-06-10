lista = ["Curso", "Python", "CodigoFacilito"]
tupla = ("Introduccion", "Basico", "Listas", "Tuplas")


mensaje = "Este es el curso de Python"

nueva_lista = list(tupla)
print(nueva_lista)

nueva_tupla = tuple(lista)
print(nueva_tupla)

string_to_list = list(mensaje)
print(string_to_list)

string_to_tuple = tuple(mensaje)
print(string_to_tuple)