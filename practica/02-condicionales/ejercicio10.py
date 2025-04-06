nombre_usuario = input("Ingrese su nombre de usuario")
contrasenia = input("Ingrese su contraseña")

if nombre_usuario == "admin" and contrasenia == "12345": 
  print("Acceso concedido")
else:
  print("Acceso denegado")