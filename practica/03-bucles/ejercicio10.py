while True: 
  pedido = input("Ingrese un pedido del menú")
  print(f"Usted a pedido {pedido}")

  continuar = input("Si desea terminar de pedir escriba salir").lower()

  if continuar == "salir":
    break
