import math


class Circular:
    """This is class of circular"""
    def __init__(self, radius):
        """Initialize the attributes of circular"""
        self.radius = radius

    def area(self):
        return round(self.radius ** 2 * math.pi, 2)  # calculate circular's area

    def circumference(self):
        return round(2 * math.pi * self.radius, 2)  # calculate circumference


class Rectangle:
    """This is class of rectangle"""
    def __init__(self, width, height):
        """Initialize the attributes of rectangle"""
        self.width = width
        self.height = height

    def area(self):
        return round(self.width * self.height, 2)  # calculate rectangle's area

    def perimeter(self):
        return round((self.width + self.height) * 2, 2)  # calculate rectangle's perimeter


class Trapezoid:
    """This is class of trapezoid"""
    def __init__(self, t_base, b_base, height):
        """Initialize the attributes of trapezoid"""
        self.t_base = t_base
        self.b_base = b_base
        self.height = height

    def area(self):
        return round((self.t_base + self.b_base) * self.height / 2, 2)  # calculate trapezoid's area


class Triangle:
    """This is class of triangle"""
    def __init__(self, base, height):
        """Initialize the attributes of triangle"""
        self.base = base
        self.height = height

    def area(self):
        return round(self.base * self.height / 2, 2)  # calculate triangle's area

# assign each class to the variables with parameter


C1 = Circular(5)
C2 = Circular(12.5)
R1 = Rectangle(6, 100)
R2 = Rectangle(13, 62)
T1 = Trapezoid(15, 20, 6)
T2 = Trapezoid(8, 60, 18)
t1 = Triangle(13, 8)
t2 = Triangle(21.5, 18)

# format the output

print('Circular 1: Area = {:.2f} Circumference = {:.2f}'.format(C1.area(), C1.circumference()))
print('Circular 2: Area = {:.2f} Circumference = {:.2f}'.format(C2.area(), C2.circumference()))
print('Rectangle 1: Area =  {:.2f} Perimeter = {:.2f}'.format(R1.area(), R1.perimeter()))
print('Rectangle 2: Area =  {:.2f} Perimeter = {:.2f}'.format(R2.area(), R2.perimeter()))
print('Trapezoid 1: Area = {:.2f}'.format(T1.area()))
print('Trapezoid 2: Area = {:.2f}'.format(T2.area()))
print('Triangle 1: Area = {:.2f}'.format(t1.area()))
print('Triangle 2: Area = {:.2f}'.format(t2.area()))
