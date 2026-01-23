import random

mazo = {"A♠": 11,"2♠": 2,"3♠": 3,"4♠": 4,"5♠": 5,"6♠": 6,"7♠": 7,"8♠": 8,"9♠": 9,"10♠": 10,"J♠": 10,"Q♠": 10,"K♠": 10,
        "A♥": 11,"2♥": 2,"3♥": 3,"4♥": 4,"5♥": 5,"6♥": 6,"7♥": 7,"8♥": 8,"9♥": 9,"10♥": 10,"J♥": 10,"Q♥": 10,"K♥": 10,
        "A♦": 11,"2♦": 2,"3♦": 3,"4♦": 4,"5♦": 5,"6♦": 6,"7♦": 7,"8♦": 8,"9♦": 9,"10♦": 10,"J♦": 10,"Q♦": 10,"K♦": 10,
        "A♣": 11,"2♣": 2,"3♣": 3,"4♣": 4,"5♣": 5,"6♣": 6,"7♣": 7,"8♣": 8,"9♣": 9,"10♣": 10,"J♣": 10,"Q♣": 10,"K♣": 10}

mazoUsado = mazo.copy() # necesito otro maso diferente, no una referencia al mismo

def RepatirCartaJugador(jugador):
    if not jugador:
        carta1 = random.choice(list(mazoUsado.keys()))
        carta2 = random.choice(list(mazoUsado.keys()))
        jugador.extend([carta1,carta2])
        del mazoUsado[carta1]
        del mazoUsado[carta2]
          
    else:
        carta = random.choice(list(mazoUsado.keys()))
        jugador.append(carta)
        del mazoUsado[carta]
    
    return jugador

def SumaTotal(cartas, mazo): 

    listaValores = []
    for carta in cartas:
        listaValores.append(mazo[carta])

    total = 0
    for valor in listaValores:
        if (11 in set(listaValores)) and (total + valor > 21):
            esAz = lambda carta: carta == 11
            aces = [carta for carta in listaValores if esAz(carta)]
            resto = [carta for carta in listaValores if not esAz(carta)]
            subTotal = sum(resto)

            if len(aces) == 2:
                total += 2
            for aces in range(len(aces)):
                if subTotal + 11 <= 21:
                    subTotal += 11
                else:
                    subTotal += 1
                    total = subTotal
                
        else:
            total += valor
        

        def contieneAz(cartas):
            for carta in cartas:
                if carta[0] == "A":
                    return True
            return False
    return total  

def PedirCarta(jugador):
    quiereOtra = input("Queres otra carta?: s/n ")
    if quiereOtra == "s":
        RepatirCartaJugador(jugador)
        print("Tus cartas son: ",jugador, " | esto suma: ",SumaTotal(jugador, mazo))
        
        if not Perdio(jugador):
            PedirCarta(jugador)
        else: 
            print("--- Perdiste --- :(")
        return 
        
    else: 
        print("Te quedate con: ",jugador, " | esto suma: ",SumaTotal(jugador, mazo))

def Perdio(jugador):
    if SumaTotal(jugador,mazo) > 21:
        return True
def BlackJack(jugador):
    if SumaTotal(jugador, mazo) == 21:
        return True


##### MAIN

def Jugar(jugador):
    print("--------- Black Jack --------- ")
    RepatirCartaJugador(jugador)
    print("Tus cartas son: -"," ".join(jugador), "- | esto suma: ",SumaTotal(jugador, mazo))
    if BlackJack(jugador):
        print("¡¡¡ GANASTE !!!")
        return
    PedirCarta(jugador)

Jugar([])