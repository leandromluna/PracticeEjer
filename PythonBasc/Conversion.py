##Conversión de temperaturas:
##Escriba un programa que convierta grados Celsius a Fahrenheit y viceversa. 
##El programa debe solicitar 
##al usuario el valor y la unidad de medida, y devolver la temperatura convertida.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad 'Celsius' o 'Fahrenheit': ").upper()
if(unidad == "CELSIUS"):
    temperatura_convertida = celsius_a_fahrenheit(temperatura)
    print(f'La {temperatura} grados Celsius equivalen a {temperatura_convertida} grados Fahrenheit')
if(unidad == "FAHRENHEIT"):
    temperatura_convertida = fahrenheit_a_celsius(temperatura)
    print(f'La {temperatura} grados Fahrenheit equivale a {temperatura_convertida} grados Celsius')