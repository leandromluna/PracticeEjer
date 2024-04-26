# Recurrencia de los elementos de una lista:
# Escriba un programa que dado una lista de elementos,
# retorne un diccionario con cada elemento como clave y el 
# número de ocurrencias de cada elemento como valor.

def contar_ocurrencias(lista):
    ocurrencias = {}

    for elemento in lista:
        if elemento in ocurrencias:
            ocurrencias[elemento] += 1
        else:
            ocurrencias[elemento] = 1
    
    return ocurrencias

mi_lista = [1,2,3,4,5,6,7,8,9,10]
resultado = contar_ocurrencias(mi_lista)
print(resultado)