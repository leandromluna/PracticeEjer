# Palíndromos:
# Escriba una función que tome una cadena de texto como argumento y 
# devuelva True si la cadena es un palíndromo (se lee igual adelante y atrás)
# y False de lo contrario.

def palindromo(char):
    cadena = char.replace(" ", "").lower()
    return cadena == cadena[::-1]
char = "Anita lava la tina"
print(palindromo(char))