class inventory:
    def __init__(self, fish, goldfish): 
        self.money = {'fish': fish, 'goldfish': goldfish}
        self.pantry = {'Frisky Bitz': 1, 'Sashimi Boat': 0}
        self.catalog = set() # the goods we have purchased
        self.placed = set() # subset of self.catalog, the goods placed in the yard
    
    def __repr__(self):
        return f'''
        money: {self.money}
        pantry: {self.pantry}
        goods we have purchased: {self.catalog}
        goods on display: {self.placed}
        '''
    
    def buy(self, item, cost): # cost input is a tuple (moneyType, price)
        moneyType, price = cost
        if self.money[moneyType] < price:
            return "not enough money"

        # buying fish exchange is a special case
        if item == "Fish Exchange":
            self.money["fish"] += 250 
            self.money['goldfish'] -= price
            return f"we exchanged {price} goldfish for 250 fish"
        if item == "Gold Fish Exchange":
            self.money["goldfish"] += 10
            self.money['fish'] -= price
            return f"we exchanged {price} fish for 10 goldfish"

        # we record the quantity of food
        if item in self.pantry:
            self.pantry[item] += 1
            self.money[moneyType] -= price
            return f"\nbought {item}. \nwe have {self.money} "

        # we add goods to self.catalog
        self.catalog.add(item)
        self.money[moneyType] -= price
        return f"\nbought {item}. \nwe have {self.money} "
    
    def placeItem(self, item, yard, position): # placing goods into the yard
        if item not in self.placed:
            if yard.itemPositions[position] == False:
                yard.itemPositions[position] = item
                self.placed.add(item)
                return f"we placed {item} at {position}."
        else:
            return f"sorry, {item} has already been placed."
    
    def removeGood(self, yard, item): # removing item from the yard
        if item in self.placed:
            for position in yard.itemPositions:
                if yard.itemPositions[position] == item:
                    yard.itemPositions[position] = False
                    if yard.catPositions[position] != False:
                        cat = yard.catPositions[position]
                        cat.generateGift(yard)
                    break
            self.placed.remove(item)
            return f"we removed{item} from {position}"
        else:
            return f"sorry, it seems like {item} has not been placed."

    def acceptGift(self, gift): # gift is a tuple: (cat, type of gift, quantity)
        cat, moneyType, amount = gift
        self.money[moneyType] += amount
        return f"{cat} gave us {amount} {moneyType}. we have {self.money} "

    def bestArrangementConditions(self):
        return (len(self.placed) == 5)

    def getInfo(self):
        return [
            self.money, "sep",
            self.pantry, "sep",
            self.catalog, "sep",
            self.placed
        ]