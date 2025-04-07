'''
1. ¿Qué es una lista?
Una lista es una colección ordenada y mutable de elementos. Esto significa que:

Ordenada: Los elementos tienen un orden definido y se accede a ellos mediante índices (empezando en 0).

Mutable: Puedes modificarla (añadir, eliminar o cambiar elementos) después de haberla creado.
'''

"""
a) Creación de listas
Las listas se definen utilizando corchetes []. Por ejemplo:
"""

numeros = [1, 2, 3, 4, 5]
saludo = ["Hola", "mundo"]

"""
b) Acceder a los elementos
"""

primer_elemento = numeros[0]  # Accede al primer elemento (1)
print(primer_elemento)

"""
c) Modificar elementos
Las listas son mutables, lo que significa que puedes cambiar un elemento especificando su índice:
"""

numeros[2] = 10  # Cambia el tercer elemento a 10
print(numeros)

"""
d) Longitud de la lista
La función len() te permite saber cuántos elementos hay en la lista:
"""
print("La lista tiene", len(numeros), "elementos.")

"""
e) Recorrer una lista
Puedes utilizar un bucle for para recorrer y procesar cada elemento de la lista:
"""

for numero in numeros:
    print(numero)
