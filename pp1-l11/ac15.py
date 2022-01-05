import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            print("Distance between two points is 0")
        else:
            distance = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
            print("Distance between points is {:}".format(distance))

p1 = Point(0, 0)
p2 = Point(0, 0)
p1 == p2