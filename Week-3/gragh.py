#from graphics import *
import graphics as g
# create circle
win = g.GraphWin("Happy Face", 200, 200)

leftPupil = g.Point(50, 75)
# leftPupil.draw(win)

rightPupil = g.Point(150, 75)
# rightPupil.draw(win)

leftEye = g.Circle(leftPupil, 25)
leftEye.setFill("white")
leftEye.setOutline("magenta")
leftEye.draw(win)
leftPupil.draw(win)

rightEye = g.Circle(rightPupil, 25)
rightEye.setFill("white")
rightEye.setOutline("magenta")
rightEye.draw(win)
rightPupil.draw(win)
# create rectangle

nose = g.Rectangle(g.Point(75, 125), g.Point(125, 150))
nose.draw(win)
# create line(mouth)
centerMouthPoint = g.Point(100, 175)
leftMouthLine = g.Line(g.Point(40, 155), centerMouthPoint)
leftMouthLine.draw(win)
rightMouthLine = g.Line(centerMouthPoint, g.Point(160, 155))
rightMouthLine.draw(win)
