palabras = ["auto", "moto", "avion", "colectivo"]

palabra_usuario = input("Ingrese una palabra: ")

encontrado = False

for palabra in palabras:
  if palabra_usuario == palabra:
    encontrado = True
    break

if encontrado:
  print("La palabra se encuentra en la lista")
else:
  print("La palabra no se encuentra en la lista")