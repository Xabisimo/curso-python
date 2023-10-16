#Ejercicio 1

numero_complejo = 3 + 4j

print(numero_complejo)
print(type(numero_complejo))

#Ejercicio 2

my_numbers = (0,1,2,3,4,5,6,7,8,9,10)
my_list = ["Xabi",True,5,5.56,4 + 3j]
my_booleans = {True,True,False}
my_dict = {"Nombre":["Alberto,Alfredo,Xabi"],"Edad":(25,23,20),"sexo":{"masculino","masculino","masculino"}}

print(my_numbers,my_list,my_booleans,my_dict)

#Ejercicio3 
import math

point_1 = (0,1)
point_2 = (1,1)
x1,y1 = point_1
x2,y2 = point_2
distancia = math.sqrt((x2 -x1)**2 +(y2-y1)**2)

print(distancia)

#Ejercicio 4
for i in range(0,101,3):
    print(i)

def multiplicacion_con_suma(a, b):
    resultado = 0
    if b < 0:
        a, b = -a, -b  # Tratamos números negativos
    for _ in range(b):
        resultado += a
    return resultado


resultado=multiplicacion_con_suma(-3, 4)
print(resultado)

#Ejercicio 5
class Triangle:
    def __init__(self, base, altura):
        self._base = base  # Atributo privado
        self._altura = altura  # Atributo privado

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value > 0:
            self._base = value
        else:
            print("La base debe ser mayor que 0")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        if value > 0:
            self._altura = value
        else:
            print("La altura debe ser mayor que 0")

    def area(self):
        return 0.5 * self._base * self._altura

# Crear un objeto Triangle
triangle = Triangle(10, 5)

# Acceder al área usando la propiedad
print(triangle.area())

# Acceder y modificar la base y la altura mediante propiedades
print(triangle.base)  # Obtiene la base
triangle.base = 8  # Modifica la base
print(triangle.base)  # Comprueba la nueva base

print(triangle.altura)  # Obtiene la altura
triangle.altura = 4  # Modifica la altura
print(triangle.altura)  # Comprueba la nueva altura
