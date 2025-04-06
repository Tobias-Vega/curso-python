"""
Las estructuras condicionales permiten que el programa tome decisiones según se cumplan o no ciertas condiciones. En Python, las sentencias condicionales más comunes son:

if: Se ejecuta el bloque de código si la condición es verdadera.

elif: (else if) Permite evaluar otra condición si la primera no se cumple.

else: Se ejecuta cuando ninguna de las condiciones anteriores es verdadera.
"""

numero = 10

if numero > 0:
    print("El número es positivo")
elif numero == 0:
    print("El número es cero")
else:
    print("El número es negativo")
