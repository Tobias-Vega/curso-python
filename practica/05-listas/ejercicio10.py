def sumar_lista(lista):
  suma = 0
  for numero in lista:
    suma += numero
  
  return suma


resultado = sumar_lista([1, 2, 5, 7, 9])

print(resultado)