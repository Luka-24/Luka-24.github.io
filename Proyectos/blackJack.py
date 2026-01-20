import random

mazo = {"A♠": 11,"2♠": 2,"3♠": 3,"4♠": 4,"5♠": 5,"6♠": 6,"7♠": 7,"8♠": 8,"9♠": 9,"10♠": 10,"J♠": 10,"Q♠": 10,"K♠": 10,
        "A♥": 11,"2♥": 2,"3♥": 3,"4♥": 4,"5♥": 5,"6♥": 6,"7♥": 7,"8♥": 8,"9♥": 9,"10♥": 10,"J♥": 10,"Q♥": 10,"K♥": 10,
        "A♦": 11,"2♦": 2,"3♦": 3,"4♦": 4,"5♦": 5,"6♦": 6,"7♦": 7,"8♦": 8,"9♦": 9,"10♦": 10,"J♦": 10,"Q♦": 10,"K♦": 10,
        "A♣": 11,"2♣": 2,"3♣": 3,"4♣": 4,"5♣": 5,"6♣": 6,"7♣": 7,"8♣": 8,"9♣": 9,"10♣": 10,"J♣": 10,"Q♣": 10,"K♣": 10}
def Jugar():
    print("Vamos jugar Black Jack !!!")
    mazoUsado = mazo
    cartaSacada, segundaCarta = random.choice(list(mazoUsado.keys())),random.choice(list(mazoUsado.keys()))
    mano = [cartaSacada,segundaCarta]
    sumarCartasJugador = mazoUsado.pop(cartaSacada) + mazoUsado.pop(segundaCarta)

    print(f"Tu mano es: {cartaSacada} y {segundaCarta} || esto suma: {sumarCartasJugador} \n")

    sigue = input("queres otra carta? s/n: ")
    while sigue == "s":
        cartaSacada = random.choice(list(mazoUsado.keys()))
        mano.append(cartaSacada)
        sumarCartasJugador += mazoUsado.pop(cartaSacada)
        print(f"sacaste un {cartaSacada} || tu mano es {mano} || esto suma: {sumarCartasJugador}\n")
        if sumarCartasJugador > 21:
            print("PERDISTE - sumaste mas de 21")
            return 
        elif sumarCartasJugador == 21:
            print("GANASTE!!!!")
        sigue = input("queres otra carta? s/n: ")
    print(f"te quedaste con {sumarCartasJugador}\n")

    print("Ahora juega la Banca")
    cartaSacada, segundaCarta = random.choice(list(mazoUsado.keys())),random.choice(list(mazoUsado.keys()))
    mano = [cartaSacada,segundaCarta]
    sumarCartas = mazoUsado.pop(cartaSacada) + mazoUsado.pop(segundaCarta)
    print(f"La banca tiene: {cartaSacada} y {segundaCarta} || esto suma: {sumarCartas} \n")
    while sumarCartas < 17:
        cartaSacada = random.choice(list(mazoUsado.keys()))
        mano.append(cartaSacada)
        sumarCartas += mazoUsado.pop(cartaSacada)
        print(f"saco un {cartaSacada} || la mano de la banca es {mano} || esto suma: {sumarCartas}\n")
    if sumarCartas > 21:
        print("LA BANCA PIERDE")
        return
    elif sumarCartas == 21:
        print("LA BANCA GANA")
        return
    print(f"la banca se queda con {sumarCartas}\n")
    print(sumarCartasJugador)
    print(sumarCartas)
    if sumarCartasJugador > sumarCartas:  
        print("GANASTE!!!!")
        return
    else:
        print("PERDISTE")
        return

    mazoUsado = mazo
    
Jugar()
