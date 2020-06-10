def crear_usuario(nombre, apellido, edad=10):
    return {
        'nombre' : nombre,
        'apellido': apellido,
        'nombre_completo': "{}{}".format(nombre,apellido),
        'edad': edad
    }

codi = crear_usuario(edad=29,nombre="Rodrigo",apellido="Montenegro")

print(codi['nombre'])    
print(codi["apellido"])
print(codi["edad"])