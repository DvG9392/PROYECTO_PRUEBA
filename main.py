import pandas as pd

saludo = "Hola"
despedida = "Adiós"

nombre = input("¿Cómo te llamas?: ")

edad=int(input("¿Cuántos años tienes?: "))

if int(edad) >= 18:
   print(saludo + ", " + nombre)

else:
   print(despedida +", " + nombre)
   print("Lo siento, no puedes entrar al sitio web.")


# Este programa saluda al usuar djdhd
print(pd.DataFrame({
"nombre" : [nombre]
}, columns=["Nombre"]))