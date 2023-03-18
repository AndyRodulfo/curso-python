# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla todos los anios que ha cumplido
# (desde 1 hasta su edad)

edad = int(input("Ingrese su edad: "))

for i in range(0, edad):
    print("Cumpliste " + str(i + 1) + " anios")
