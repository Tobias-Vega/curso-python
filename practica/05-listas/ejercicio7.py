numeros = [2, 4, 5, 6, 9, 3]
maximo = numeros[0]

for numero in numeros:
  if numero > maximo:
    maximo = numero

print("El mayor de los números es:", maximo)