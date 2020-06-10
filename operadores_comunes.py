lista = [8.17, 90, 1, 5, 44, 1.32, 90]

lista.sort(reverse=True)
mayor = lista[0]
menor = min(lista)
longitud = len(lista)

resultado = 8.17 in lista
indice = lista.index(5)
contador = lista.count(90)


print(lista)
print(mayor)
print(menor)
print("Longitud",longitud)
print(resultado)
print(indice)
print(contador)

