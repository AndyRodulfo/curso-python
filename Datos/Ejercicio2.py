Practico1 = float(input('Nota del primer practico:'))  
Practico2 = float(input('Nota del segundo practico:'))
Practico3 = float(input('Nota del tercer practico:'))

PromedioPractico = ((Practico1+Practico2+Practico3)/3)

ExamenParcial = float(input('Nota del Examen Parcial:'))

ExamenFinal = float(input('Nota examen final:'))

PromedioSemestre = (PromedioPractico+(2*ExamenParcial)+(3*ExamenFinal))/6

print('Promedio del Semestre del estudiante:\n',PromedioSemestre, '\nPromedio de los practicos del estudiante:\n', PromedioPractico)