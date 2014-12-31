
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
    return True


# Tests
print True == isHidden(Point(0, 0), Point(20, 0), Body(5, Point(10, 0)))
print False == isHidden(Point(0, 0), Point(10, 0), Body(5, Point(20, 0)))
print False == isHidden(Point(0, 0), Point(20, 20), Body(5, Point(10, 0)))
print False == isHidden(Point(0, 0), Point(20, -20), Body(5, Point(10, 0)))
