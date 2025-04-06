temperatura = float(input("Ingrese la temperatura actual: "))

if temperatura < 15:
  print("Frío")
elif temperatura >= 15 and temperatura <= 25:
  print("Templado")
else:
  print("Caluroso")