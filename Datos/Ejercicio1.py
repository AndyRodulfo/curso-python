from math import sqrt

a = float(input('Valor de a:'))
b = float(input('Valor de b:'))
c = float(input('Valor de c:'))

x1=0
x2=0

if((b**2)-(4*a*c))<0:
    print('no se puede realizar dado que es un numero negativo')
else:
    x1=((-b+sqrt((b**2)-(4*a*c)))/(2*a))
    x2=((-b-sqrt((b**2)-(4*a*c)))/(2*a))
print('La solución es: \nx1=', x1)
print('La solución es: \nx2=', x2)
