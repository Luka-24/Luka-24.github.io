import random

mazo = {"A♠": 11,"2♠": 2,"3♠": 3,"4♠": 4,"5♠": 5,"6♠": 6,"7♠": 7,"8♠": 8,"9♠": 9,"10♠": 10,"J♠": 10,"Q♠": 10,"K♠": 10,
        "A♥": 11,"2♥": 2,"3♥": 3,"4♥": 4,"5♥": 5,"6♥": 6,"7♥": 7,"8♥": 8,"9♥": 9,"10♥": 10,"J♥": 10,"Q♥": 10,"K♥": 10,
        "A♦": 11,"2♦": 2,"3♦": 3,"4♦": 4,"5♦": 5,"6♦": 6,"7♦": 7,"8♦": 8,"9♦": 9,"10♦": 10,"J♦": 10,"Q♦": 10,"K♦": 10,
        "A♣": 11,"2♣": 2,"3♣": 3,"4♣": 4,"5♣": 5,"6♣": 6,"7♣": 7,"8♣": 8,"9♣": 9,"10♣": 10,"J♣": 10,"Q♣": 10,"K♣": 10}

mazoUsado = mazo.copy() # necesito otro maso diferente, no una referencia al mismo

def RepartirCartas(jugador):
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
        RepartirCartas(jugador)
        print("Tus cartas son: -"," ".join(jugador), "- | esto suma: ",SumaTotal(jugador, mazo))
        
        if not Perdio(jugador):
            PedirCarta(jugador)
        else: 
            print("--- Perdiste --- :(")
        return 
        
    else: 
        print("Te quedate con: -"," ".join(jugador), "- | esto suma: ",SumaTotal(jugador, mazo))

def Perdio(jugador):
    if SumaTotal(jugador,mazo) > 21:
        return True
def BlackJack(jugador):
    if SumaTotal(jugador, mazo) == 21:
        return True

def JuegaCrupier(crupier):
    total = SumaTotal(crupier,mazo)
    while total < 17:
        RepartirCartas(crupier)
        print("-- La mesa pide carta")
        total = SumaTotal(crupier,mazo)
        if total > 21:
            print("El crupier tiene: -"," ".join(crupier), "- | esto suma",SumaTotal(crupier, mazo))
            print("LA MESA PIERDE, GANASTE!!!!")
            break
        elif total >= 17:
            print("El crupier se queda con: -"," ".join(crupier), "- | esto suma: ",total,)
            break
        else:
            print("El crupier tiene: -"," ".join(crupier), "- | esto suma",SumaTotal(crupier, mazo))

##### MAIN

def Jugar(jugador,crupier):
    print("--------- Black Jack --------- ")
    RepartirCartas(jugador)
    RepartirCartas(crupier)
    print("Tus cartas son: -"," ".join(jugador), "- | esto suma: ",SumaTotal(jugador, mazo))
    soloPrimeraCarta = crupier[0] 
    print("El crupier tiene: -","".join(soloPrimeraCarta), "[?] -")
    if BlackJack(jugador):
        print("¡¡¡ GANASTE !!!")
        return
    PedirCarta(jugador)
    #### CRUPIER
    if not Perdio(jugador):
        print("- Truno del Crupier -")
        print("El crupier tiene: -"," ".join(crupier), "- | esto suma",SumaTotal(crupier, mazo))
        JuegaCrupier(crupier)
    


jugador,crupier = [],[]
Jugar(jugador,crupier)