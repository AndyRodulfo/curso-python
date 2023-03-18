diccionario={"Guatemala":"Ciudad de Guatemala", "Honduras":"Tegucigalpa","Nicaragua":"Managua","Costa Rica":"San Jose","Panama":"Panama","Argentina":"Buenos Aires","Colombia":"Bogota","Venezuela":"Caracas","España":"Madrid","El-r.Salvador":"San Salvador"}

pais = input("Ingrese un país para conocer su capital:")
letra = pais.capitalize() in diccionario

if letra == True:
    print(diccionario[pais.capitalize()])
else:
    print("El pais que seleccionaste no se encuentra en el diccionario.")