diccionario = {"a":1, "b":2, "c":3, "a":4}

resultado = "Z" in diccionario
get = diccionario.get("a", "La llave no existe")
poner = diccionario.setdefault("z",{})


print(diccionario)
print(resultado)
print(get)