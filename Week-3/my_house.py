import graphics as g
win = g.GraphWin("My House ", 1000, 800)
# Draw House


def drawHouse():
    House = g.Rectangle(g.Point(40, 120), g.Point(660, 580))
    House.draw(win)
    House.setOutline("Green")

# Draw two rectangles


def drawRectangles():
    drawTwoRectangles = g.Rectangle(g.Point(90, 220), g.Point(220, 310))
    drawTwoRectangles.draw(win)
    drawTwoRectangles.setOutline("Blue")
    drawTwoRectangles = drawTwoRectangles.clone()
    drawTwoRectangles.move(380, 0)
    drawTwoRectangles.draw(win)


def drawLastRectangle():
    lastRectangle = g.Rectangle(g.Point(200, 330), g.Point(450, 580))
    lastRectangle.draw(win)
    lastRectangle.setOutline("Blue")

# Drw two line


def drawTwoLines():
    centerLine = g.Point(330, 8)
    leftLine = g.Line(g.Point(30, 50), centerLine)
    leftLine.draw(win)
    RightLine = g.Line(g.Point(650, 30), centerLine)
    RightLine.draw(win)

# Draw circle


def drawCircle():
    circleCenter = g.Point(900, 100)
    circle = g.Circle(circleCenter, 50)
    circle.draw(win)
    win.getMouse()
    circle.setFill("Red")

# Draw text label


def textLabel():
    textBox = g.Text(g.Point(360, 200), "Nice house")
    textBox.setOutline("Grey")
    textBox.draw(win)

# Print out


def printOut():
    drawHouse()
    drawRectangles()
    drawLastRectangle()
    drawTwoLines()
    drawCircle()
    textLabel()


printOut()
drawHouse()
drawRectangles()
drawLastRectangle()
drawCircle()
drawTwoLines()
textLabel()
