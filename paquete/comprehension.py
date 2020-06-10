#lista = []
#
#for x in range(0,101):
#    lista.append(x)
#
#print(lista)

estructura = [ x for x in range(0,101) ] # la primera x es el valor a almacenar
print(estructura)

estructura_tupla = tuple ((x for x in range(0,101) 
                             if x % 2 == 0 ))

print (estructura_tupla)

diccionario = { indice:valor
                for indice, valor in  enumerate(estructura_tupla)}

print(diccionario)