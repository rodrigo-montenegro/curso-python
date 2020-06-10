animal = "Leon"  #variable global

def mostrar_animal():
    global animal
    animal = "Ballena" #variable local
    print(animal)

mostrar_animal()
print(animal)