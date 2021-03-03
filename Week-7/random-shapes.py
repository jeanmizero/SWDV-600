import random
from graphics import *


# Inputs
fileName = input("Enter the drawing file name to create: ")
numberOfShapes = int(input("Enter the number of shapes to make: "))
# open file
file = open(fileName, "w")
for i in range(numberOfShapes):
    # shape random
    type = random.randint(0, 1)
    # rectangle shape
    if type == 0:
        leftCoordinate = [random.randint(0, 499), random.randint(0, 499)]

        while leftCoordinate[0] == 499 and leftCoordinate[499] == 0:
            leftCoordinate = [random.randint(0, 499), random.randint(0, 499)]

        rightCoordinate = [random.randint(
            leftCoordinate[0] + 1, 499), random.randint(leftCoordinate[1] + 1, 499)]
        redIntensity = random.randint(0, 100)
        greenIntensity = random.randint(100, 200)
        blueIntensity = random.randint(192, 255)

        if i == numberOfShapes - 1:
            file.write("Rectangle; "+str(leftCoordinate[0])+", "+str(leftCoordinate[1])+"; "+str(rightCoordinate[0])+", "+str(
                rightCoordinate[1])+"; "+str(redIntensity)+", "+str(greenIntensity)+", "+str(blueIntensity))
        else:
            file.write("Rectangle; "+str(leftCoordinate[0])+", "+str(leftCoordinate[1])+"; "+str(rightCoordinate[0])+", "+str(
                rightCoordinate[1])+"; "+str(redIntensity)+", "+str(greenIntensity)+", "+str(blueIntensity)+"\n")

        # circle shape
    else:

        center = [random.randint(0, 499), random.randint(0, 499)]
        if center[0] > center[1]:

            radius = random.randint(0, 499-center[0])
        else:
            radius = random.randint(0, 499-center[1])
        redIntensity = random.randint(0, 100)
        greenIntensity = random.randint(100, 200)
        blueIntensity = random.randint(192, 255)

        if i == numberOfShapes - 1:  # last record
            file.write("Circle; "+str(center[0])+", "+str(center[1])+"; "+str(
                radius)+"; "+str(redIntensity)+", "+str(blueIntensity)+", "+str(greenIntensity))
        else:
            file.write("Circle; "+str(center[0])+", "+str(center[1])+"; "+str(radius)+"; "+str(
                redIntensity)+", "+str(blueIntensity)+", "+str(greenIntensity)+"\n")

file.close()


def getColor(colorString):
    tokens = colorString.split(',')
    if len(tokens) == 3:
        return color_rgb(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    elif len(colorString) > 0:
        return colorString.strip()
    else:
        return "white"


def getPoint(pointString):
    x, y = pointString.split(',')
    return Point(int(x), int(y))


def getRadius(radiusString):
    return int(radiusString)


def parseRectangleLine(line):
    shapeStr, ulPtStr, lrPtStr, colorStr = line.split(";")
    ulPt = getPoint(ulPtStr)
    lrPt = getPoint(lrPtStr)
    color = getColor(colorStr)

    rectangle = Rectangle(ulPt, lrPt)
    rectangle.setFill(color)

    return rectangle


def parseCircleLine(line):
    shapeStr, centerPtStr, radiusStr, colorStr = line.split(';')
    centerPt = getPoint(centerPtStr)
    radius = getRadius(radiusStr)
    color = getColor(colorStr)

    circle = Circle(centerPt, radius)
    circle.setFill(color)
    return circle


def getShapeName(line):
    tokens = line.split(";")
    return tokens[0]


def getShapes(drawingFile):
    shapes = []
    lineNumber = 0

    for line in drawingFile:
        lineNumber = lineNumber + 1
        shapeName = getShapeName(line)
        shape = None

        if shapeName.casefold() == 'circle'.casefold():
            shape = parseCircleLine(line)

        elif shapeName.casefold() == 'rectangle'.casefold():
            shape = parseRectangleLine(line)
        else:
            raise ValueError(
                'ERROR on line {0}: Invalid shape {1}'.format(lineNumber, shapeName))
        shapes.append(shape)
    return shapes


def drawShapes(shapes):
    win = GraphWin("Drawing", 500, 500)

    for shape in shapes:
        shape.draw(win)


def main():
    # get file name
    fileName = input("Enter the drawing file name: ")
    # open the file
    drawingFile = open(fileName, 'r')
    # get the shapes
    shapes = getShapes(drawingFile)
    # draw the shapes
    drawShapes(shapes)


main()

# end of program
