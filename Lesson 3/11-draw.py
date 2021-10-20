import math

#dikdörtgen çizme
def printRectangle(height,width):
    for i in range(height):
        print("* "*width)

#kare çizme
def printSquare(edgeSize):
    printRectangle(edgeSize,edgeSize)

#daire çizme
def calculateIfPointIsInRadius(i, j, radius):
    centerX = radius
    centerY = radius
    pointDistance = math.sqrt(abs(j - centerX))**2 + abs((i - centerY)**2)
    if abs(pointDistance - radius) < 0.3:
        return True
    return False
#-------------------
def drawCircle(radius):
    for i in range((radius * 2)+1):
        for j in range((radius * 2)+1):
            if calculateIfPointIsInRadius(i, j, radius):
                print("* ",end="")
            else:
                print("  ",end="")
        print()

print(drawCircle(10))