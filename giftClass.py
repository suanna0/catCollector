class Gift:
    def __init__(self, gift): # gifts are inputted as tuples. example: (snowball, "goldfish", 15) 
        self.givenFrom = gift[0]
        self.moneyType = gift[1]
        self.quantity = gift[2]

    def getHashables(self):
        return (self.givenFrom, self.moneyType, self.quantity)

    def __repr__(self):
        return f"{self.getHashables()}"

    def __hash__(self):
        return hash(self.getHashables())
    
    def receive(self, inventory):
        inventory.money[self.moneyType] += self.quantity