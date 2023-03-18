tupla = (1,2,3,4,5)
tupla2=6,7,8,9,10
#a diferencia de la lista, los datos no se pueden modificar
print(tupla)
print(type(tupla))

print(tupla[2])
print(tupla[0:3]) #el de la derecha nunca es tomado
print(tupla + tupla2)
'''
tupla[2] = 10
print(tupla)            ERROR ya que no se puede modificar
'''