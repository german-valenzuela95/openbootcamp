import math

peso=float(input("Ingrese su peso en kg:"))
estatura=float(input("Ingrese su Estatura en Metros:"))

imc =round(peso/math.pow(estatura,2),2)

print("Tu Indice DeMasa Corporal Es: " + str(imc))

