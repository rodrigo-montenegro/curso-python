tupla = (1,2,3,4,5,6)
lista = [10,20,30,40]
tupla_dos = (100,200,300,400)

uno, dos, tres, *cuatro = tupla

resultado = zip(tupla,lista,tupla_dos)
resultado = tuple(resultado)

print(uno)
print(dos)
print(tres)
print(cuatro)

print(resultado)