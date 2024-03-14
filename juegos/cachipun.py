from random import randint
def cachipun():
    print("Bienvenido al juego más popular ""cachipun"". Te enfrentaras a la poderosa computadora, para comenzar selecciona ""piedra"", ""papel"" o ""tijera"")
    jugador=input()
    print("Seleccionaste "+jugador)
    a=randit(0,2)
    if a==0:
        computadora="tijeras"
    elif a==1:
        computadora="papel"
    else:
        computadora="roca"
    if (jugador=="tijeras" and computadora=="papel") or (jugador=="roca" and computadora=="tijeras") or (jugador=="papel" and computadora=="roca"):
        print("¡Has ganado a la computadora!")
    elif (computadora=="tijeras" and jugador=="papel") or (computadora=="roca" and jugador=="tijeras") or (computadora=="papel" and jugador=="roca"):
        print("¡Has perdido contra la computadora!")
    else:
        print("¡Has empatado con la computadora!")
    pass