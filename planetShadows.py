import math


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
def isHidden(p1, p2, b):
    q = math.asin(b.radius/(b.center.x-p1.x)) # angle from p1 to external tangent of body
    print q
    k = math.atan((p2.y-p1.y)/(p2.x-p1.x)) # angle from p1 to p2
    print k
    return True

# Tests
print True == isHidden(Point(0.0, 0.0), Point(20.0, 0.0), Body(5.0, Point(10.0, 0.0)))
print False == isHidden(Point(0.0, 0.0), Point(10.0, 0.0), Body(5.0, Point(20.0, 0.0)))
print False == isHidden(Point(0.0, 0.0), Point(20.0, 20.0), Body(5.0, Point(10.0, 0.0)))
print False == isHidden(Point(0.0, 0.0), Point(20.0, -20.0), Body(5.0, Point(10.0, 0.0)))

# makin a change