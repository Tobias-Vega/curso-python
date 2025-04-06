def cuadrado(num):
  return num ** 2

def suma_cuadrados(num1, num2):
  cuadrado1 = cuadrado(num1)
  cuadrado2 = cuadrado(num2)

  return cuadrado1 + cuadrado2

print(f"La suma de los cuadrados es: {suma_cuadrados(3, 2)}")