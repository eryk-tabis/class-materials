class Area(object):
    @staticmethod
    def circle(radius):
        return radius ** 2 * 3.14

    @staticmethod
    def rectangle(side1, side2):
        return side1 * side2

    @staticmethod
    def triangle(base, height):
        return (base * height) / 2

print(Area.circle(3))
print(Area.rectangle(4, 7))
print(Area.triangle(6, 2))
