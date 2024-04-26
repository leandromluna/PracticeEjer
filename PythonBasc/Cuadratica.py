# Función cuadrática:
# Escriba un programa que resuelva una ecuación cuadrática de la forma ax^2 + bx + c, 
# los coeficientes a, b y c son proporcionadas por el usuario.
import math

def f_cuadratica(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "La ecuacion no tiene soluciones reales."
    elif discriminante == 0:
        x = -b / (2*a)
        return f"La solucion unica es x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Las soluciones son x1 = {x1} y x2 = {x2}"

v_a = int(input("Ingrese el valor de a: "))
v_b = int(input("Ingrese el valor de b: "))
t_ind = int(input("Ingrese el valor del termino independiente: "))
print(f_cuadratica(v_a,v_b,t_ind))

