texto = "   curso de Python 3, Python basico    "

mayuscula = texto.capitalize()
swap = texto.swapcase()
todo_mayuscula = texto.upper()
minuscula = texto.lower()
titulo = texto.title()
reemplazo = texto.replace("Python","Ruby",1)
sin_espacios =  texto.strip()


print(mayuscula)
print(swap)
print(todo_mayuscula)
print(minuscula)

print(todo_mayuscula.isupper())

print(titulo)
print(reemplazo)
print(sin_espacios)