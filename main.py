from JeudeCartes import JeudeCartes, Paquets            #all imports
from Joueurs import Joueur1, Joueur2, Dealer
from random import randint
import time

def calculgain(jp,dp,joueur,nbcartej,mise):             #gains or losses (jp = player's points, dp = dealer's points, mise = bet)
    if jp > 21:                                         #if player's points over 21
        joueur.setgain(joueur.getgain()-mise)           #take away the bet amount from the gains of player 
        gagne = -1                                      #take away 1 point from varibale win
    elif dp > 21:                                       #if dealer's point over 21
        if jp == 21 and nbcartej == 2:                  #if player has 21 points with 2 cards only (BlackJack)
            joueur.setgain(joueur.getgain()+2*mise)     #add to the player's gain double the bet
        else:
            joueur.setgain(joueur.getgain()+mise)       #else add to the player's gain the bet amount
        gagne = 1                                       #variable win = 1

    elif jp < 21 and dp < 21:                           #if both player and dealer under 21
        if jp > dp:                                     #if player points greater than dealer's points
            joueur.setgain(joueur.getgain()+mise)       #add to the player's gain the bet amount
            gagne = 1                                   #variable win = 1
        elif jp < dp:                                   #if player points less than dealer's points
            joueur.setgain(joueur.getgain()-mise)       #take away to the player's gain the bet amount
            gagne = -1                                  #variable win = -1
        else:
            gagne = 0                                   #else variable win = 0

    else:
        if dp == 21 and jp != 21:                       #if dealer is 21
            joueur.setgain(joueur.getgain()-mise)       #take away to the player's gain the bet amount
            gagne = -1                                  #variable win = -1
        elif jp == 21 and dp != 21:                     #if player is 21
            if nbcartej == 2:                           #if 2 cards only
                joueur.setgain(joueur.getgain()+2*mise)         #add to the player's gain double the bet
            else:
                joueur.setgain(joueur.getgain()+mise)           #add to the player's gain the bet amount
            gagne = 1                                   #variable win = 1
        else:
            gagne = 0                                   #variable win = 0
    return joueur, gagne                                #return player and win variables

def parties():                                          #games
    tours = randint(15,20)                              #random number of rounds between 15 and 20
    #tours = 6
    p = Paquets(8)                                      #with 8 decks
    joueur1 = Joueur1()
    joueur2 = Joueur2()
    dealer = Dealer()
    mise2 = 1                                           #the bets
    mise1 = 1

    for i in range(5):
        p.distribue()                           
    for t in range(tours):
        joueur1.setmvide()
        joueur2.setmvide()
        dealer.setmvide()
        for d in range(2):
            joueur1.prendrecarte(p.distribue())
            joueur2.prendrecarte(p.distribue())
            dealer.prendrecarte(p.distribue())

        #print(joueur1.getm())
        while joueur1.strategie():
            joueur1.prendrecarte(p.distribue())
            #print(joueur1.getm())

        continuer = True
        while continuer:
            js2 = joueur2.strategie(dealer.getm()[0])
            if js2 == "H":
                joueur2.prendrecarte(p.distribue())
            elif js2 == "S":
                continuer = False
            elif js2 == "D":
                mise2 = 2*mise2
                joueur2.prendrecarte(p.distribue())

        #print(' ')

        #print(dealer.getm())
        while dealer.strategie():
            dealer.prendrecarte(p.distribue())
            #print(dealer.getm())

        jp = joueur1.points()
        jp2 = joueur2.points()
        dp = dealer.points()
        nbcartej = len(joueur1.getm())
        nbcarted = len(dealer.getm())
        nbcartej2 = len(joueur2.getm())
        joueur1,gagne1 = calculgain(jp,dp,joueur1,nbcartej,mise1)
        joueur2,gagne2 = calculgain(jp2,dp,joueur2,nbcartej2,mise2)

        if gagne2 == 1:
            mise2 = 1
        elif gagne2 == -1:
            mise2 = mise2*2

        if gagne1 == 1:
            mise1 = 1
        elif gagne1 == -1:
            mise1 = mise1*2

        #Joueur place un pari sur BlackJack / Player places a bet on BlackJack

        """if dealer.getm()[0][0] == 11:
            if dp == 21:
                joueur1.setgain(joueur1.getgain()+1)
            else:
                joueur1.setgain(joueur1.getgain()-1)"""


        #print('La main du joueur est', joueur1.getm())
        #print('La main du dealer est', dealer.getm())
        #print('Le score du joueur est', jp)
        #print('Le score du dealer est', dp)
        #print('Les points du joueur sont', joueur1.getgain())
    #print(tours)
    #print(joueur1.getgain())
    return joueur1.getgain(),joueur2.getgain()

pg1 = 0
pg2 = 0
s = 0
x = int(input('Input number:'))

top = time.time()
for k in range(x):
    g1,g2 = parties()
    if g1 > 0:
        pg1 += 1
    if g2 > 0:
        pg2 += 1
    s += g2
stop = time.time()

duree = stop - top

print(pg1/x)                            #probability to win game 1
print(pg2/x)                            #probability to win game 2
print(s/x)
print(duree)                            #time it took to calculate (very bad running time...)

#Ecrire tous les cas possibles
# -de 21, + de 21, = 21

#Ace is first set as 11 point card and whenever the score seems to cross 21, 
#we can reduce the score of ace to 1


