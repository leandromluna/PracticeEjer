##Saludo personalizado:
##Escriba un programa que pida al usuario su nombre y edad, 
##luego imprima un saludo personalizado que incluya su nombre y su edad.

def saludo(a,b):
    print(f'Hola {a.title()}, como estas? Tu edad es de {int(b)}')

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
saludo(nombre,edad)