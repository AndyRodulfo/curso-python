palabra1 = input("Inserte la primera palabra: ")
palabra2 = input("Inserte la segunda palabra: ")

if len(palabra1)<3 or len(palabra2)<3:
    print("No rima porque tiene menos de 3 caracteres")
elif palabra1[-3: ] == palabra2[-3: ]:
    print("Las palabras riman")
elif palabra1[-2:] == palabra2[-2: ]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")