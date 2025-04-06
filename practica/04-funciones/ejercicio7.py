def es_bisiesto(anio):
  return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


print(f"El año 2020 es bisiesto {es_bisiesto(2020)}")
print(f"El año 2018 es bisiesto: {es_bisiesto(2018)}")