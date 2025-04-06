"""
Las funciones son bloques de código reutilizables que realizan una tarea específica. Permiten que el código sea modular, organizado y más fácil de mantener. Además, ayudan a evitar la repetición de código.

1. Definición y uso de funciones
a) ¿Qué es una función?
Una función es un bloque de código que se ejecuta cuando es llamado.

Puedes pasarle datos a la función a través de parámetros.

Puede devolver un valor mediante la palabra clave return.
"""

# Sintaxis básica
def nombre_de_la_funcion(parametro1, parametro2):
    # Bloque de código
    resultado = parametro1 + parametro2  # Ejemplo de operación
    return resultado  # Devuelve el resultado


"""
c) Llamar a una función
Para utilizar la función, basta con llamarla y, si es necesario, capturar su valor de retorno:
"""

suma = nombre_de_la_funcion(3, 4)
print(suma)  # Esto imprimirá 7 en el ejemplo anterior


"""
Conceptos clave en funciones
a) Parámetros y argumentos
Parámetros: Variables que se definen en la declaración de la función.

Argumentos: Valores reales que se pasan a la función al momento de llamarla.

b) Valor de retorno
La declaración return finaliza la ejecución de la función y devuelve el valor especificado.

Si no se especifica un return, la función devuelve None por defecto.

c) Funciones sin parámetros ni retorno
Es posible definir funciones que no reciben parámetros o no devuelven valores, por ejemplo, funciones que solo muestran información en pantalla.
"""
def saludar():
    print("¡Hola a todos!")

saludar()  # Llamada a la función

"""
Ámbito de las variables (scope)
Las variables locales se definen dentro de una función y solo son accesibles allí.

Las variables globales se definen fuera de cualquier función y pueden ser utilizadas en todo el programa, aunque su uso dentro de funciones se debe manejar con cuidado para evitar conflictos.
"""

"""
Funciones lambda (anónimas)
Son funciones pequeñas sin nombre, definidas con la palabra clave lambda y utilizadas generalmente para operaciones simples.
"""

suma = lambda a, b: a + b
print(suma(5, 3))  # Imprime 8
