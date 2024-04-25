#Desafíos del día! Introducción a la Programación con Python de nivel principiante... 
#Calculadora Básica:
#Escriba un programa que pida al usuario dos números y 
#luego muestre en pantalla el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.

def sum(a, b):
    return a + b
def rest(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
print(sum(numero,numero2))
print(rest(numero,numero2))
print(mult(numero,numero2))
print(div(numero,numero2))


