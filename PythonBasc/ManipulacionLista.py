# Manipulación de listas:
# Cree una lista de 5 elementos y realice las siguientes operaciones:
# Añade un elemento al principio y al final de la lista.
# Ordena la lista de mayor a menor.
# Elimina el tercer elemento de la lista.
# Diccionario de colores:
# Cree un diccionario donde las claves sean nombres de 
# colores y los valores sean la longitud de cada palabra. 
# Presente los resultados en un formato de cadena ordenada.

numeros = [1,2,3,4,5]
numeros.insert(0,15)
numeros.append(20)
numeros.sort()
print(numeros)

numeritos = {
    "Verde": len("Verde"),
    "Amarillo": len("Amarillo")
}
largo_colores = {
    color: longitud for color, longitud in numeritos.items()
}
resultado = ",".join([f'{color}: {longitud}' for color, longitud in largo_colores.items()])
print(resultado)