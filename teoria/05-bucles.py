"""
Un bucle (o loop) permite ejecutar un bloque de código varias veces de forma automática, mientras se cumpla una condición o para recorrer elementos.
"""

"""
🔄 Tipos de bucles en Python:
1. while: Repite mientras una condición sea verdadera.
"""

contador = 0
while contador < 5:
  print("Contador:", contador)
  contador += 1


"""
for: Recorre elementos de una secuencia (listas, cadenas, rangos, etc).
"""

for i in range(5):
    print("Valor:", i)

"""
🔧 Funciones útiles para bucles for:
range(inicio, fin, paso): genera una secuencia de números.

range(1, 5) → 1, 2, 3, 4

range(0, 10, 2) → 0, 2, 4, 6, 8

len(lista): devuelve la cantidad de elementos.

enumerate(lista): devuelve índice y valor.
"""

"""
🔁 Control de bucles
break: interrumpe el bucle.

continue: salta a la siguiente iteración.

else en bucles: se ejecuta si el bucle no fue interrumpido con break.
"""