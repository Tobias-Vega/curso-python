intentos = 3
contrasenia_correcta = "Admin"

while True : 
  contrasenia = input("Ingrese la contraseña")

  if contrasenia == contrasenia_correcta:
    print("Contraseña correcta")
    break
  else: 
    print("Contraseña incorrecta")
    intentos -= 1

  if intentos == 0:
    print("Límite de intentos, acceso denegado")
    break