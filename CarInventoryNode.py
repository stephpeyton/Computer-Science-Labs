#car inventory node
from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make
        self.model = car.model
        self.parent = None
        self.left = None
        self.right = None
        self.cars = []
        self.cars.append(car)

    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
        return False
            
    def __lt__(self, rhs):
        if rhs > self:
            return True
        else:
            return False
        
    def __eq__(self, rhs):
        return (self.make == rhs.make) and (self.model == rhs.model)
                 
            
    def getMake(self):
        return self.make
        
    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        cars_str = ""
        for c in self.cars:
            cars_str += c.__str__() + "\n"
        return cars_str


