# Rectangle 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Object of Rectangle
rectangle = Rectangle(5, 3)
print("Area of the rectangle:", rectangle.area())
