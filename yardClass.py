class yard: 
    def __init__(self, L): # input L is the hardcoded list of positions
        # name of position is the key. False = position is empty
        self.itemPositions = dict() # key = position, value = item
        self.catPositions = dict() # key = position, value = cat (object)
        self.itemPositionsList = [] # list for drawing stuff, as there is a particular order to be followed.
        for position in L:
            self.itemPositions[position] = False
            self.catPositions[position] = False
            self.itemPositionsList.append(position)
        self.food = None # the food that is currently in the yard
        self.foodLevel = 0

    def __repr__(self): # for debugging purposoes 
        return f'''
        ordered list of positions: {self.itemPositionsList}
        positions filled: {self.itemPositions}
        food out: {self.food}
        '''

    def spawnCatsConditions(self): # returns True if there is food and there is an item out
        if self.food != None and self.foodLevel > 0:
            for position in self.itemPositions:
                if self.itemPositions[position] != False:
                    return True
        return False
    
    def spawn(self, cat, normalItems, rareItems, normalCats, rareCats):
        if self.spawnCatsConditions() == True:
            for position in self.itemPositions:
                if self.itemPositions[position] != False: # check that there is a position with an item
                    item = self.itemPositions[position]
                    if self.catPositions[position] == False: # check that there is no cat in that position
                        if (item in normalItems and cat.name in normalCats) or (item in rareItems and cat.name in rareCats):
                            self.catPositions[position] = cat
                            cat.visiting = True
                            cat.visits += 1
                            cat.visitTime = 0 
                            cat.timeToLeave = cat.generateTimeToLeave()
                            cat.itemsFrequency[item] = cat.itemsFrequency.get(item, 0) + 1
                            if self.food == "Frisky Bitz": # Frisky Bitz runs out twice as fast as sashimi boat
                                self.foodLevel -= 2
                            elif self.food == "Sashimi Boat":
                                self.foodLevel -= 1
                            if self.foodLevel == 0:
                                self.food = None
                        return None
        return None

    def forceSpawn(self, position, cat): 
        item = self.itemPositions[position]
        self.catPositions[position] = cat
        cat.visiting = True
        cat.visits += 1
        cat.visitTime = 0
        cat.timeToLeave = cat.generateTimeToLeave()
        cat.itemsFrequency[item] = cat.itemsFrequency.get(item, 0) + 1
        if self.food == "Frisky Bitz": # Frisky Bitz runs out twice as fast as sashimi boat
            self.foodLevel -= 2
        elif self.food == "Sashimi Boat":
            self.foodLevel -= 1
        if self.foodLevel == 0:
            self.food = None
        return None



    def checkOpenSpots(self): # returns False if all spots are filled
        openSpots = False
        for position in self.itemPositions:
            if self.itemPositions[position] == False: # then we have an open spot
                openSpots = True
        return openSpots
    
    def getInfo(self):
        for position in self.catPositions:
            if self.catPositions[position] != False: # save as name, not as object
                cat = self.catPositions[position]
                self.catPositions[position] = cat.name
        return [
            self.itemPositions, "sep",
            self.catPositions, "sep",
            self.itemPositionsList, "sep",
            self.food, "sep",
            self.foodLevel
        ]