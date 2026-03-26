saludo = "Hola"
despedida = "Adiós"

nombre = input("¿Cómo te llamas?: ")

edad=int(input("¿Cuántos años tienes?: "))

if int(edad) >= 18:
   print(saludo + ", " + nombre)

else:
   print(despedida +", " + nombre)


# Este programa saluda al usuar
