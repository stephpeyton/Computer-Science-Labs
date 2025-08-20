from Car import Car
from CarInventoryNode import *
from CarInventory import *
def test_example():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getTotalInventoryPrice() == 158000

    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
        
def test_example():
    assert bst.inOrder() == \
"Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

    assert bst.preOrder() == \
"Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"

    assert bst.postOrder() == \
"Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n"

def test_example():
    assert bst.getBestCar("Honda", "Accord") == car4
    assert bst.getBestCar("Jeep", "Wrangler") == None
    assert bst.getWorstCar("Honda", "Accord") == car1
    assert bst.getWorstCar("Jeep", "Wrangler") == None
