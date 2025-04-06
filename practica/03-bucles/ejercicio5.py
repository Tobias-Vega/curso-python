numero_secreto = 15

while True:
  numero = int(input("Adivina el número secreto"))

  if numero == numero_secreto:
    print("Felicidades, adivinaste el número")
    break