import random
from fractions import Fraction

def pickPoint():
    randX = -13
    randY = -13
    while randX == randY and randX != 0 :
        randX = random.randint(-12, 12)
        randY = random.randint(-12,12)    
    poi = [randX, randY]
    return poi
def lineCreator(point):
    print(f"POI at {point}")
    randB2 = 0
    changeX = 0
    while changeX == 0:
        randB = random.randint(-12, 12)
        changeY = randB - point[1]
        changeX = 0 - point[0]
        slope = Fraction(changeY, changeX)
    print(f"The first equation is y = {slope}x + {randB}")
    print(f"Kinda Standard Form is: {-1*changeY}x + {(changeX)}y = {randB * changeX} ")

    changeX2 = 0
    randB2 = 0
    while randB2 == 0:
        randB2 = random.randint(-12, 12)
    changeY2 = 0 - point[1]
    changeX2 = randB2 - point[0]
    slope2 = Fraction(changeY2, changeX2)
    print(f"The second equation is y = {slope2}x + {randB2}")
    print(f"Kinda Standard Form is: {-1*changeY2}x + {(changeX2)}y = {randB2 * changeX2} ")        

def main():
    mainPOI = pickPoint()
    lineCreator(mainPOI)

main() #does this actually work??
#dfasd