diccionario = {
1:"Casillas" , 15: "Ramos" ,
3: "Pique" , 5: "Puyol" ,
11: "Capdevila" , 14: "Xavi Alonso" ,
16: "Busquets" , 8:"Xavi Hernandez",
18 : "Pedrito", 6:"Iniesta",
7:"Villa"
}

OpcionJugador= int(input("Elige un numero para revelar el jugador al que pertenece:"))

if OpcionJugador in diccionario:
    print("El numero que seleccionaste corresponde a" , diccionario[OpcionJugador])
else:
    print("El número que seleccionaste no corresponde a un jugador")