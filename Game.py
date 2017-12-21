from random import shuffle

gameDim = 5

class Player:
    def __init__(self):
        self.staging = [ (None, 0) for i in range(gameDim) ]
        self.board   = [[ 0 for i in range(gameDim)] for i in range(gameDim) ]

class Game:
    def __init__(self, players = 2):
        self.bag = { i:20 for i in range(gameDim) }
        numPlacards = { 2:5, 3:6, 4:7 }
        self.placards = [ self.emptyDict() for x in range(numPlacards[players]) ]
        self.middle = self.emptyDict()
        self.garbage = self.emptyDict()
        self.players = [ Player() for i in range(players) ]
        self.deal() 

    def emptyDict(self):
        result = { i:0 for i in range(gameDim) }
        return result

    # Takes a piece dictionary like {1:4, 2:0, 3:1, ..} 
    #  and returns [1,1,1,1,3, ..]
    def flattenDict(self, aDict):
        result = []
        for k, v in aDict.items():
            for i in range(v): result.append(k)
        return result

    # Does the opposite of above
    def dictifyList(self, aList):
        result = {}
        for x in aList:
            if x in result: result[x] += 1
            else: result[x] = 1
        return result

    def deal(self):
        # Flatten bag
        bag = self.flattenDict(self.bag)
        shuffle(bag)
        for i, el in enumerate(self.placards):
            if (len(bag) < 4): 
                garbage = self.flattenDict(self.garbage)
                self.garbage = { i:0 for i in range(gameDim) }
                bag = bag + garbage
                shuffle(bag)

            if (len(bag) < 4):
                print("Still don't have enough pieces.")
                raise bag
        
            placard = bag[-4:]
            bag = bag[:-4]
            print(placard)
            print(bag)
            self.placards[i] = self.dictifyList(placard)
        self.bag = self.dictifyList(bag)

    def __str__(self):
        result = "Bag: " + str(self.bag) + "\n"
        result += "Placards: \n"
        for i, el in enumerate(self.placards):
            result += "\t" + str(i) + ". " + str(el) + "\n"
        result += "Middle: " + str(self.middle) + "\n"
        result += "Garbage: " + str(self.garbage) + "\n"
        result += "Players: " + "\n"
        for p in self.players:
            result += "\t" + str(p) + "\n"
        return result
       
g = Game(2)
print(g)
