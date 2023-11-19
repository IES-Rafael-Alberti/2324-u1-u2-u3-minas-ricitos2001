import random

#impresion del cuadro
def colocar_cuadro(jugador_cuadro):
    simbolos={-2:"F", -1:"·"}
    impresion=""
    for fila in range(len(jugador_cuadro)):
        for columna in range(len(jugador_cuadro[fila])):
            valor=jugador_cuadro[fila][columna]
            if valor in simbolos:
                simbolo=simbolos[valor]
            else:
                simbolo=str(valor)
            impresion+=simbolo+" "
        impresion+="\n"
    return impresion


# añadir la bandera al cuadro de manera aleatoria
def añadir_bandera_cuadro(cuadro,vacio,bandera):
    fila=random.randint(0, 8)
    columna=random.randint(0, 8)
    if cuadro[fila][columna] == vacio:
        cuadro[fila][columna] = bandera
        # si pierdes
        añadir_bandera="se añadio una bandera en la fila "+str(fila)+" y columna "+str(columna)
        return añadir_bandera
    else:
        # si ganas
        return añadir_bandera_cuadro(cuadro,vacio,bandera)

# contar posiciones
def contador(fila,columna):
    contador=0
    compensaciones=((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
    for compensacion in compensaciones:
        compensacion_fila=fila+compensacion[0]
        compensacion_columna=columna+compensacion[1]
        if (compensacion_fila>=0 and compensacion_fila<=8) and (compensacion_columna>=0 and compensacion_columna<=8):
            if cuadro[compensacion_fila][compensacion_columna]==mina:
                contador+=1
    return contador

# introducir posicion
def clickear_cuadro(fila,columna):
    celdas=[(fila,columna)]
    compensaciones=((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
    while len(celdas)>0:
        celda=celdas.pop()
        for compensacion in compensaciones:
            fila=compensacion[0]+celda[0]
            columna=compensacion[1]+celda[1]
            if (fila>=0 and fila<=8) and (columna>=0 and columna<=8):
                if((jugador_cuadro[fila][columna]==desconocido) and (cuadro[fila][columna]==vacio)):
                    jugador_cuadro[fila][columna]=contador(fila,columna)
                    if contador(fila,columna)==vacio and (fila, columna) not in celdas:
                        celdas.append((fila,columna))
                    else:
                        jugador_cuadro[fila][columna]=contador(fila,columna)
                        return jugador_cuadro

# verificar si has ganado o no
def verificar_victoria(fila,columna):
    if cuadro[fila][columna]==mina:
        mensaje="has explotado"
    elif cuadro[fila][columna] == bandera:
        mensaje="has ganado"
    return mensaje

if __name__=="__main__":
    # entradas
    vacio=0
    mina=1
    bandera=-2
    desconocido=-1
    # impresion del cuadro oculto
    cuadroaleatorio1=[]
    cuadroaleatorio2=[]
    cuadroaleatorio3=[]
    cuadroaleatorio4=[]
    cuadroaleatorio5=[]
    cuadroaleatorio6=[]
    cuadroaleatorio7=[]
    cuadroaleatorio8=[]
    cuadroaleatorio9=[]
    cuadro=[cuadroaleatorio1,cuadroaleatorio2,cuadroaleatorio3,cuadroaleatorio4,cuadroaleatorio5,cuadroaleatorio6,cuadroaleatorio7,cuadroaleatorio8,cuadroaleatorio9]
    for i in range(9):
        numeroaleatorio1=random.randint(0, 1)
        numeroaleatorio2=random.randint(0, 1)
        numeroaleatorio3=random.randint(0, 1)
        numeroaleatorio4=random.randint(0, 1)
        numeroaleatorio5=random.randint(0, 1)
        numeroaleatorio6=random.randint(0, 1)
        numeroaleatorio7=random.randint(0, 1)
        numeroaleatorio8=random.randint(0, 1)
        numeroaleatorio9=random.randint(0, 1)
        cuadroaleatorio1.append(numeroaleatorio1)
        cuadroaleatorio2.append(numeroaleatorio2)
        cuadroaleatorio3.append(numeroaleatorio3)
        cuadroaleatorio4.append(numeroaleatorio4)
        cuadroaleatorio5.append(numeroaleatorio5)
        cuadroaleatorio6.append(numeroaleatorio6)
        cuadroaleatorio7.append(numeroaleatorio7)
        cuadroaleatorio8.append(numeroaleatorio8)
        cuadroaleatorio9.append(numeroaleatorio9)
    print(cuadro)
    # impresion del cuadro de juego
    jugador_cuadro=[
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    ]
    # añadir la bandera
    añadir_bandera=añadir_bandera_cuadro(cuadro,vacio,bandera)
    ejecucion=True
    while ejecucion:
        impresion=colocar_cuadro(jugador_cuadro)
        print(impresion)
        print(añadir_bandera)
        fila=int(input("introduce un numero del 0 al 8: "))
        columna=int(input("introduce otro numero del 0 al 8: "))
        click=clickear_cuadro(fila,columna)
        print(click)
        # comprobar si la partida ha terminado o no
        if (cuadro[fila][columna]==mina) or (cuadro[fila][columna] == bandera):
            mensaje=verificar_victoria(fila,columna)
            print(mensaje)
            ejecucion=False
        elif jugador_cuadro[fila][columna]==desconocido:
            jugador_cuadro[fila][columna]=contador(fila,columna)
            ejecucion=True
