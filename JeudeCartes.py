from random import randint

class JeudeCartes:

    def __init__(self):
        self.c = []                                 #empty list to contain all elements in deck of cards
        l = [2,3,4,5,6,7,8,9,10,10,10,10,11]        #all possible card amounts in one deck of cards (J,Q,K all = 10)
        for n in l:
            for s in range(4):                      #in order to add each element 4 times because 4 different suits
                self.c.append((n,s))                #tuple: (the amount on card, its suit)

    def getjeu(self):
        return self.c

class Paquets:

    def __init__(self,n):                           #initialize
        self.p = []
        for i in range(n):
            j = JeudeCartes()
            self.p += j.getjeu()
        self.melange(n)

    def getpaquet(self):                            #get function
        return self.p

    def melange(self,n):                            #shuffling of the cards
        for m in range(n*20000):                    #in order to shuffle, loop through actions a very big number of times
            a = randint(0,len(self.p)-1)            # a = random number in deck
            b = randint(0,len(self.p)-1)            # b = random number in deck
            self.p[a],self.p[b] = self.p[b],self.p[a]       #switch places

    def distribue(self):
        return self.p.pop(0)                        #using pop, distributes cards from deck


#6 jeux de cartes avec 5 premières brulées
#6 card decks, with the first 5 cards unused

#jeu = Paquets(6)
#jeu.getpaquet()
