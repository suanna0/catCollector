class yardPosition:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def __repr__(self):
        return(self.name)
    
    def coordinates(self):
        return((self.x, self.y))