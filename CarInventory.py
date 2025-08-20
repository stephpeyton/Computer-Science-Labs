#car inventory
from CarInventoryNode import CarInventoryNode

from Car import Car


class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root:
            self._addCar(CarInventoryNode(car), self.root)
        else:
            self.root = CarInventoryNode(car)

    def _addCar(self, newNode, currentNode):
        if newNode == currentNode:
            currentNode.cars.append(newNode.cars[0])
        elif newNode < currentNode:
            if currentNode.getLeft():
                self._addCar(newNode, currentNode.getLeft)
            else:
                currentNode.setLeft(newNode)
                newNode.setParent(currentNode)
        else:
            if currentNode.getRight():
                self._addCar(newNode, currentNode.getRight)
            else:
                currentNode.setRight(newNode)
                newNode.setParent(currentNode)



    def doesCarExist(self, car):
        res = self._doesCarExist(CarInventoryNode(car), self.root)
        if res:
            for i in res.cars:
                if i == car:
                    return True
        return False
            

    def _doesCarExist(self, newNode, currentNode):
        if not currentNode:
            return None
        elif currentNode == newNode:
            return currentNode
        elif newNode < currentNode:
            return self._doesCarExist(newNode, currentNode.left)
        else:
            return self._doesCarExist(newNode, currentNode.right)
            
        
    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += self._inOrder(currentNode.left)
            ret += currentNode.__str__()
            ret += self._inOrder(currentNode.right)
        return ret

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += currentNode.__str__()
            ret += self._preOrder(currentNode.left)
            ret += self._preOrder(currentNode.right)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += self._postOrder(currentNode.left)
            ret += self._postOrder(currentNode.right)
            ret += currentNode.__str__()
        return ret


            
    
    def getBestCar(self, make, model):
        s = Car(make, model, 0, 0)
        carNode = CarInventoryNode(s)
        end = self._doesCarExist(carNode, self.root)
        if end:
            best = end.cars[0]
            for i in end.cars:
                if i > best:
                    best = i
            return best
        return end
    

    def getWorstCar(self, make, model):
        s = Car(make, model, 0, 0)
        carNode = CarInventoryNode(s)
        end = self._doesCarExist(carNode, self.root)
        if end:
            worst = end.cars[0]
            for i in end.cars:
                if i < worst:
                    worst = i
            return worst
        return end

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)
        

    def _getTotalInventoryPrice(self, currentNode):
        total = 0
        if currentNode is not None:
            for i in currentNode.cars:
                total += i.price
            total += self._getTotalInventoryPrice(currentNode.left)
            total += self._getTotalInventoryPrice(currentNode.right)
        return total



    
        
