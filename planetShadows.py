import math
import random
import time


# Point has a simple (x,y)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Planetary bodies have a center and a radius
class Body:
    def __init__(self, r, c):
        self.radius = r
        self.center = c

# Function checks whether or not p2 (Point)
# is hidden from p1 (Point) behind b (Body)
def isHiddenA(p1, p2, b):
    shipToPlanetDist = math.sqrt(pow(b.center.x - p1.x, 2) + pow(b.center.y - p1.y, 2))
    shipToEnemyDist = math.sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))

    # not that this should ever happen...
    if shipToPlanetDist < b.radius:
        return True

    # is p2 further away from p1 than b
    if shipToEnemyDist < shipToPlanetDist:
        return False

    tangentLineAngleWithShipToPlanetAxis = math.asin(b.radius / shipToPlanetDist)
    scalarProjection = ((p2.x - p1.x) * (b.center.x - p1.x) + (p2.y - p1.y) * (b.center.y - p1.y)) / (shipToPlanetDist * shipToEnemyDist)

    # p2 is in opposite direction from p1 than b
    if (scalarProjection <= 0):
        return False

    enemyShipAngleWithShipToPlanetAxis = math.acos(scalarProjection)
    return tangentLineAngleWithShipToPlanetAxis > enemyShipAngleWithShipToPlanetAxis

# Function checks whether or not p2 (Point)
# is hidden from p1 (Point) behind b (Body)
def isHiddenB(p1, p2, b):
    # rotate space to put b on the x axis
    shipToPlanetDist = math.sqrt(pow(b.center.x - p1.x, 2) + pow(b.center.y - p1.y, 2))

    # not that this should ever happen...
    if shipToPlanetDist < b.radius:
        return True

    planetTheta = math.atan2((b.center.y-p1.y), (b.center.x-p1.x))
    p2tx, p2ty = RotateByTheta(p2.x-p1.x, p2.y-p1.y, planetTheta)

    # if p2 isn't behind the leading edge of b relative to p1 it is not hidden
    if p2tx < (shipToPlanetDist-b.radius):
        return False

    angleToExternalTangent = math.asin(b.radius/shipToPlanetDist)
    angleToP2t = math.atan(p2ty/p2tx)
    return abs(angleToP2t) < angleToExternalTangent

def RotateByTheta(x, y, t):
    ct = math.cos(t)
    st = math.sin(t)
    return ct*x + st*y, -st*x + ct*y

# Tests
# print True == isHiddenA(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, 0.0)))
# print False == isHiddenA(Point(0.0, 0.0), Point(10.0, 0.0), Body(5.0, Point(20.0, 0.0)))
# print False == isHiddenA(Point(0.0, 0.0), Point(20.0, 20.0), Body(5.0, Point(10.0, 0.0)))
# print False == isHiddenA(Point(0.0, 0.0), Point(20.0, -20.0), Body(5.0, Point(10.0, 0.0)))
# print False == isHiddenA(Point(0.0, 0.0), Point(-20.0, 20.0), Body(5.0, Point(10.0, 0.0)))

print False == isHiddenA(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, 10.0)))
print True == isHiddenA(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, 0.0)))
print False == isHiddenA(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, -10.0)))

print False == isHiddenA(Point(0.0, 0.0), Point(-20.0, 20.0), Body(5.0, Point(10.0, 10.0)))
print False == isHiddenA(Point(0.0, 0.0), Point(-20.0, 0.0), Body(5.0, Point(10.0, 0.0)))
print False == isHiddenB(Point(0.0, 0.0), Point(-20.0, -20.0), Body(5.0, Point(10.0, -10.0)))


print False == isHiddenB(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, 10.0)))
print True == isHiddenB(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, 0.0)))
print False == isHiddenB(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, -10.0)))

print False == isHiddenB(Point(0.0, 0.0), Point(-20.0, 20.0), Body(5.0, Point(10.0, 10.0)))
print False == isHiddenB(Point(0.0, 0.0), Point(-20.0, 0.0), Body(5.0, Point(10.0, 0.0)))
print False == isHiddenB(Point(0.0, 0.0), Point(-20.0, -20.0), Body(5.0, Point(10.0, -10.0)))

runs = 1000000
strt = time.clock()
for _ in range(runs):
    isHiddenA(Point(random.random()*200-100, random.random()*200-100),
        Point(random.random()*200-100, random.random()*200-100),
        Body(random.random()*5+0.00001, Point(random.random()*200-100, random.random()*200-100)))
print time.clock() - strt

strt = time.clock()
for _ in range(runs):
    isHiddenB(Point(random.random()*200-100, random.random()*200-100),
        Point(random.random()*200-100, random.random()*200-100),
        Body(random.random()*5+0.00001, Point(random.random()*200-100, random.random()*200-100)))
print time.clock() - strt

# makin a change AGAIN :D

# ShipToPlanetDist = sqrt(X_Planet - X_Ship) ^ 2 + (Y_Planet - Y_Ship) ^ 2)
# ShipToEnemyDist = sqrt((X_Enemy - X_Ship) ^ 2 + (Y_Enemy - Y_Ship) ^ 2)
# TangentLineAngleWithShipToPlanetAxis = arcsin(PlanetRadius / ShipToPlanetDist)
# EnemyShipAngleWithShipToPlanetAxis = arccos( ((X_Enemy - X_Ship) * (X_Planet - X_Ship) + (Y_Enemy - Y_Ship) * (Y_Planet - Y_Ship)) ...
# 					/ (ShipToPlanetDist * ShipToEnemyDist))