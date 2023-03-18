candidato = input('Vote a un candidato, seleccionando con la letra "A" al partido rojo, con la letra "B" al partido verde y con la letra "C" al partido azul:\n')

if candidato.upper() == "A":
    print('Usted ha votado por el partido ROJO')
elif candidato.upper() == "B":
    print('Usted ha votado por el partido VERDE')
elif candidato.upper() == "C":
    print('USted ha votado por el partido AZUL')
else:
    print('Opción Erronea!')