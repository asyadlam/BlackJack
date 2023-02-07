#I've decided to use 2 players and the dealer
#the 1st player has the same strategy as the dealer
#the 2nd player has a different strategy (la martingale)

#Stratégie comme Dealer (1st player)

class Joueur1:                              #in this code, Joueur1 is considered to play with the same strategy as the Dealer

    def __init__(self):
        self.m = []
        self.gain = 0

    def prendrecarte(self,c):
        self.m.append(c)

    def getm(self):
        return self.m

    def getgain(self):
        return self.gain

    def setgain(self,g):
        self.gain = g

    def points(self):                       #returns amount of points (sum of both cards)
        s = 0
        ln = []
        for i in range(len(self.m)):
            s += self.m[i][0]
            ln.append(self.m[i][0])
        while s > 21:                       #while sum is over 21
            if 11 in ln:                    #check if there's an 11 in the cards
                s -= 10                     #if so, take out 10 to make the 11 a 1 (This because Ace card can either be an 11 or a 1)
                ln[ln.index(11)] = 1        #replaces the 11 with the 1 in the list
            else:
                break
        return s                            #returns the total sum of two cards

    def strategie(self):                    #returns true if need of another card and false otherwise
        s = self.points()
        if s <= 16 and len(self.getm()) < 6:        #usually, if your sum is <= 16, you take another one (max of 5 cards in hand)
            return True
        return False

    def setmvide(self):
        self.m = []

#Stratégie autre (other strategy, being the martingale)

class Joueur2:                               #in my code, Joueur2 is a player playing with a certain strategy (different from dealer)

    def __init__(self):
        self.m = []
        self.gain = 0

    def prendrecarte(self,c):
        self.m.append(c)

    def getm(self):
        return self.m

    def getgain(self):
        return self.gain

    def setgain(self,g):
        self.gain = g

    def points(self):                        #returns amount of points (sum of both cards)
        s = 0
        ln = []
        for i in range(len(self.m)):        #go through the list
            s += self.m[i][0]               #add to the sum the card's amount at position i
            ln.append(self.m[i][0])         #add to the list that same number
        while s > 21:                       #while sum is greater than 21
            if 11 in ln:                    #if the number 11 is in the list (in your hand)
                s -= 10                     #take away 10 from the sum total
                ln[ln.index(11)] = 1        #replace number 11 with a 1 in your hand (an ace can be either 1 or 11)
            else:
                break                       #else, bust
        return s                            #return the sum

    def strategie(self,cartedealer):        #very detailed strategy found on internet
        main = self.getm()
        if len(main) == 2 and main[0][0] == main[1][0]:         #if 2 cards in hand, and they're both same amount
            if main[0][0] == 8 or main[0][0] == 11:             #if they're both 8 or both 11
                #return "SP"                                    #strategy is to split (SP), however, I changed it to hit (H)
                return "H"
            if main[0][0] == 5:              #if double 5
                return "D"                   #double down (D)
            if main[0][0] == 10:             #if double 10
                return "S"                   #stand (S)
            if main[0][0] == 2 or main[0][0] == 3 or main[0][0] == 7:           #if both are 2,3,7
                if cartedealer[0] <= 7:                                         #if dealer s card is less or equal to 7
                    #return "SP"                                                #strategy says to split, but I decided to just hit
                    return "H"
                else:
                    return "H"                                                  #else, hit (H)
            if main[0][0] == 6:                                                 #if double 6
                if cartedealer[0] <= 6:                                         #if dealer s card is less or equal to 6
                    #return "SP"                                                #strategy says to split, but I decided to just hit
                    return "H"
                else:
                    return "H"                                                  #else, hit (H)
            if main[0][0] == 4:
                if cartedealer[0] == 5 or cartedealer[0] == 6:                  #same for the following, I decided to return hit anyways and not split
                    #return "SP"
                    return "H"
                else:
                    return "H"
            if main[0][0] == 9:                                                 #same here, except i decided to stand instead of split
                if cartedealer[0] == 7 or cartedealer[0] >= 10:
                    return "S"
                else:
                    #return "SP"
                    return "S"
        elif len(main) == 2 and main[0][0] == 11:                               #if 2 cards in hand, and the first one is 11
            if main[1][0] >= 8:                                                 #if second is greater or equal to 8
                return "S"                                                      #stand
            if main[1][0] == 2 or main[1][0] == 3:                              #if second card is 2 or 3
                if cartedealer[0] == 5 or cartedealer[0] == 6:                  #depending on the dealer's 1st card (card that is showing)
                    return "D"                                                  #double down
                else:
                    return "H"                                                  #else, hit
            if main[1][0] == 4 or main[1][0] == 5:                              #same thing for the following "if statements"
                if cartedealer[0] == 5 or cartedealer[0] == 6 or cartedealer[0] == 4:
                    return "D"
                else:
                    return "H"
            if main[1][0] == 6:
                if cartedealer[0] == 2 or cartedealer[0] >= 7:
                    return "H"
                else:
                    return "D"
            if main[1][0] == 7:
                if cartedealer[0] >= 3 and cartedealer[0] <= 6:
                    return "D"
                elif cartedealer[0] == 9 or cartedealer[0] == 10:
                    return "H"
                else:
                    return "S"
        elif len(main) == 2 and main[1][0] == 11:
            if main[0][0] >= 8:
                return "S"
            if main[0][0] == 2 or main[0][0] == 3:
                if cartedealer[0] == 5 or cartedealer[0] == 6:
                    return "D"
                else:
                    return "H"
            if main[0][0] == 4 or main[0][0] == 5:
                if cartedealer[0] == 5 or cartedealer[0] == 6 or cartedealer[0] == 4:
                    return "D"
                else:
                    return "H"
            if main[0][0] == 6:
                if cartedealer[0] == 2 or cartedealer[0] >= 7:
                    return "H"
                else:
                    return "D"
            if main[0][0] == 7:
                if cartedealer[0] >= 3 and cartedealer[0] <= 6:
                    return "D"
                elif cartedealer[0] == 9 or cartedealer[0] == 10:
                    return "H"
                else:
                    return "S"
        else:                                
            p = self.points()               #amount the points of cards in hand
            if p >= 17:                     #if points are greater or euqal to 17, stand (similar for following "if statements")                      
                return "S"
            elif p >= 13:
                if cartedealer[0] <= 6:     #still also depends on dealer's showing card
                    return "S"
                else:
                    return "H"
            elif p >= 5 and p <= 8:
                return "H"
            elif p == 9:
                if cartedealer[0] >= 3 and cartedealer[0] <= 6:
                    return "D"
                else:
                    return "H"
            elif p == 10:
                if cartedealer[0] >= 10:
                    return "H"
                else:
                    return "D"
            elif p == 11:
                if cartedealer[0] == 11:
                    return "H"
                else:
                    return "D"
            else:
                if cartedealer[0] >= 4 and cartedealer[0] <= 6:
                    return "S"
                else:
                    return "H"

    def setmvide(self):
        self.m = []

#The dealer does not have a choice, when his cards add up to 16 or lower, 
#he has to hit, whereas when his cards add up to 17 or more, he stands

class Dealer:                               #in this code, Joueur1 is considered the Dealer of the Game (Specific strategy)
                                            #very straightforward strategy
    def __init__(self):
        self.m = []

    def prendrecarte(self,c):
        self.m.append(c)

    def getm(self):
        return self.m

    def points(self):
        s = 0
        ln = []
        for i in range(len(self.m)):
            s += self.m[i][0]
            ln.append(self.m[i][0])
        while s > 21:
            if 11 in ln:
                s -= 10
                ln[ln.index(11)] = 1
            else:
                break
        return s

    def strategie(self): #retourne true si besoin d une autre carte et false sinon
        s = self.points()
        if s <= 16 and len(self.getm()) < 6:
            return True         #returns true if need for another card
        return False            #false if no need

    def setmvide(self):
        self.m = []








