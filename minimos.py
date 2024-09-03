import random

def funcion(x,y):
    p1 = (1.5 - x + (x*y))**2
    p2 = (2.25 - x + (x*(y)**2))**2
    p3 = (2.625 - x + (x*(y)**3))**2
    return p1 + p2 + p3

funcion_minima = 1
funcion_actual = 0

for i in range(10000): #Se hacen las iteraciones
    valor_x = random.uniform(-4.5, 4.5) #Generar valor aleatorio decimal entre -4.5 y 4.5
    valor_y = random.uniform(-4.5, 4.5)

    funcion_actual = funcion(valor_x, valor_y) #se asigna el valor de la funcion a otra variable para simplificar

    if funcion_actual < funcion_minima: #se compara el valor de la funcion actual con un valor minimo.
        funcion_minima = funcion_actual #se asigna ese valor nuevo ahora como minimo
        print(f"funcion({valor_x}, {valor_y}) = {funcion_minima}") #se imprime el valor de x,y, el valor de la funcion
    

