from giftClass import *

def reverseDict(d): # helper function
    result = dict()
    for key in d:
        value = result.get(d[key], set())
        value.add(key)
        result[d[key]] = value
    return result

def pythag(x0, x1, y0, y1): # helper function
    return int(((x1-x0)**2 + (y1 - y0)**2)**(1/2))

import random

class cat:
    def __init__(self, name, breed, personality, powerLevel, favoriteItem, favoritePosition):
        self.name = name
        self.breed = breed
        self.personality = personality
        self.powerlevel = powerLevel
        self.visits = 0
        self.itemsFrequency = dict()
        self.favoriteItem = favoriteItem
        self.favoritePosition = favoritePosition
        self.visiting = False # when true, cat will be in yard
        self.visitTime = None 
        self.timeToLeave = 0 # randomly generated, from 5 mins to 1 hour
    
    def generateTimeToLeave(self):
        minutes = random.randint(5, 60)
        return minutes*600 # multiply seconds and timerDelay

    def updateTime(self, app, yard):
        self.visitTime += 1 
        if self.visitTime >= self.timeToLeave:
            gift = Gift(self.generateGift(yard)) # cat leaves yard
            app.giftsNotReceived.append(gift)
        return None

    def calculateGift(self, item, position, favoriteSpotCoordinates):
        visitedFavoriteItem = False
        visitedFavoritePosition = False
        if item == self.favoriteItem: 
            visitedFavoriteItem = True
        if position.name == self.favoritePosition: 
            visitedFavoritePosition = True
        # cat gives a lot of goldfish when they visit their favorite spot, regardless of power level
        if visitedFavoriteItem == True and visitedFavoritePosition == True:
            quantity = random.randint(20, 30)
            gift = (self.name, "goldfish", quantity)
        else:
            x, y, z = 0, 0, 0
            if visitedFavoriteItem == True: x = 10
            x0, y0 = position.coordinates()
            x1, y1 = favoriteSpotCoordinates
            distance = pythag(x0, x1, y0, y1) 
            # get distance from position vs preferred position
            x = (250 - distance)//100 #250 is the approximate maximum distance
            y = self.powerlevel
            z = self.visits
            quantity = x*y + z + 3 # algebraic expression generates gift. 
            # cat will give at least 3 fish
            if self.powerlevel < 50: # the cat is not rare. we get less fish
                moneyType = "fish"
            else: # cat is rare, generate fish type based on parity of visits
                if self.visits%2 == 0:
                    moneyType = "fish"
                else:
                    moneyType = "goldfish"
                    quantity //= 2 # make quantity lower if cat gives goldfish
            gift = (self.name, moneyType, quantity)
        return gift 

    def generateGift(self, yard):
        self.visiting = False
        positionToEnter = None
        for position in yard.catPositions:
            if yard.catPositions[position] == self:
                item = yard.itemPositions[position]
                yard.catPositions[position] = False
                positionToEnter = position
        # get coordinates of favorite position
        coordinatesDict = {"bench": (193, 297), "porch": (75, 380), "carpet (back)": (245, 465), "carpet (front)": (129, 510), "stump": (275, 525)}
        favoriteSpotCoordinates = coordinatesDict[self.favoritePosition]
        gift = self.calculateGift(item, positionToEnter, favoriteSpotCoordinates)
        return gift 
    
    def getTop3(self): # returns string to print on cat profile
        reversedTopGoodies = reverseDict(self.itemsFrequency) # frequencies become the key 
        listOfFreq = []
        for key in reversedTopGoodies:
            listOfFreq.append(key)
        listOfFreq.sort()
        greatestFreq = listOfFreq[-1]
        secondFreq = thirdFreq = None
        if len(listOfFreq) >= 3:
            secondFreq, thirdFreq = listOfFreq[-2], listOfFreq[-3]
        elif len(listOfFreq) >= 2:
            secondFreq = listOfFreq[-2]
        top3List = []
        while len(top3List) < 3:
            for item in reversedTopGoodies[greatestFreq]:
                if len(top3List) == 3:
                    break
                if item not in top3List: top3List.append(item)
            if secondFreq != None:
                for item in reversedTopGoodies[secondFreq]:
                    if len(top3List) == 3:
                        break
                    if item not in top3List: top3List.append(item)
                if thirdFreq != None:
                    for item in reversedTopGoodies[thirdFreq]:
                        if len(top3List) == 3:
                            break
                        if item not in top3List: top3List.append(item)
            break
        string = ''
        for i in range(len(top3List)):
            string += top3List[i]
            if i != len(top3List) - 1:
                string += ', \n'
        return string
    
    def getInfo(self):
        return([
            self.visits, 
            self.itemsFrequency, 
            self.visiting, 
            self.visitTime, 
            self.timeToLeave
        ])

    def updateInfo(self, visits, itemsFrequency, visiting, visitTime, timeToLeave):
        self.visits = visits
        self.itemsFrequency = itemsFrequency
        self.visiting = visiting
        self.visitTime = visitTime
        self.timeToLeave = timeToLeave