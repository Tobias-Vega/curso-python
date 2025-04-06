

cantidad_notas = int(input("Ingrese el número de notas: "))
suma = 0

for i in range(1, cantidad_notas + 1):
  nota = float(input(f"Ingrese la nota n° {i}: "))

  suma += nota

promedio = suma / cantidad_notas

print(f"El promedio de notas es de: {promedio}")