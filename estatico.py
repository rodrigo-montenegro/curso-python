class Triangulo:

    @staticmethod
    def area(base,altura):
        return(base * altura) / 2

resultado = Triangulo.area(10,20)
print(resultado)