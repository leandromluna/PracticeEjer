# Juego de adivinación de números:
# Escriba un programa que genere un número aleatorio del 1 al 10 y pida al usuario 
# que intente adivinarlo. 
# El programa debe continuar hasta que el usuario adivine correctamente el número.
import random

def numero_aleatoreo():
    numero_aleatoreo = random.randint(0,100)
    intentos = 0

    while intentos < 50:
        intento = int(input("Trate de adivinar un numero entre el 0 y el 100: "))
        intentos += 1

        if intento == numero_aleatoreo:
            print("Ganaste. Acertaste al numero generado")
            return
        elif intento < numero_aleatoreo:
            print("El numero es mayor")
        else:
            print("El numero es menor")

    print(f'Agotaste los intentos. El numero era {numero_aleatoreo}')

    

numero_aleatoreo()
