print("Bienvenido a la isla, Tu mision sera encontrar el tesoro")
opcion=input("derecha o izquierda")

if(opcion=="derecha"):
    print("Caiste en un agujero, Game Over")

elif(opcion=="izquierda"):
    opcion=input("arriba o abajo")

if(opcion=="arriba"):
    print("Vuelves a empezar")
    opcion=input("derecha o izquierda")

elif(opcion=="abajo"):
    opcion=input("nadar o esperar")
    if(opcion=="nadar"):
        opcion=input("derecha o izquierda")
    elif(opcion=="esperar"):
        print("Escoje una puerta: ")
        opcion=input("Azul Rojo Amarillo Verde")
        if(opcion=="Azul"):
            print("Devorado por bestias, Game Over")
        elif(opcion=="Rojo"):
            print("Eres quemado, Game Over")
        elif(opcion=="Amarillo"):
            print("Ganaste")
        elif(opcion=="Verde"):
            print("Entra a una cueva")
            print("¿Encender la antorcha?")
            opcion=input("si o no")
            if(opcion=="si"):
                print("Ganaste")
            elif(opcion=="no"):
                print("Mordido por una serpiente,Game Over")
        if(opcion=="derecha"):
            print("Atacado por una tribu, Game Over")
        elif(opcion=="izquierda"):
            print("Entra a una cueva")
            print("¿Encender la antorcha?")
            opcion=input("si o no")
            if(opcion=="si"):
                print("Ganaste")
            elif(opcion=="no"):
                print("Mordido por una serpiente,Game Over")
