from random import shuffle

gameDim = 5

class Player:
    def __init__(self):
        self.staging = [ (None, 0) for i in range(gameDim) ]
        self.board   = [[ 0 for i in range(gameDim)] for i in range(gameDim) ]

class Game:
    def __init__(self, players = 2):
        self.bag = [ 20 for i in range(gameDim) ]
        numPlacards = { 2:5, 3:6, 4:7 }
        self.placards = [ self.emptyList() for x in range(numPlacards[players]) ]
        self.middle = self.emptyList()
        self.garbage = self.emptyList()
        self.players = [ Player() for i in range(players) ]
        self.deal() 

    def emptyList(self):
        result = [ 0 for i in range(gameDim) ]
        return result

    # Takes a piece list like [4, 0, 1, ..]
    #  and returns [1,1,1,1,3, ..]
    def explodeList(self, el):
        result = []
        for i, v in enumerate(el):
            for x in range(v): result.append(i)
        return result

    # Does the opposite of above
    def compressList(self, aList):
        result = self.emptyList()
        for x in aList: result[x] += 1
        return result

    # Shuffles the bag
    # For each Placard:
    #   If there is enough tiles in the bag, put the last 4 on the placard;
    #   Otherwise add the garbage to the bag and reshuffle.
    def deal(self):
        # Flatten bag
        bag = self.explodeList(self.bag)
        shuffle(bag)
        for i, el in enumerate(self.placards):
            if (len(bag) < 4): 
                garbage = self.explodeList(self.garbage)
                self.garbage = { i:0 for i in range(gameDim) }
                bag = bag + garbage
                shuffle(bag)

            if (len(bag) < 4):
                raise bag
        
            placard = bag[-4:]
            bag = bag[:-4]
            self.placards[i] = self.compressList(placard)
        self.bag = self.compressList(bag)

    def prettyList(self, aList):
        result = ""
        for i, v in enumerate(aList):
            result += "{0:3d}\t".format(v)
        return result

    def __str__(self):
        result = "\t\t"
        for i in range(gameDim):
            result += "{0:3d}\t".format(i)
        result += "\n"
        result += "Bag:\t\t" + self.prettyList(self.bag) + "\n"
        result += "Placards:\n"
        for i, el in enumerate(self.placards):
            result += "\t\t" + str(i) + ".\t" + self.prettyList(el) + "\n"
        result += "Middle:\t\t" + self.prettyList(self.middle) + "\n"
        result += "Garbage:\t" + self.prettyList(self.garbage) + "\n"
        result += "Players: " + "\n"
        for p in self.players:
            result += "\t" + str(p) + "\n"
        return result
       
g = Game(2)
print(g)
