class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle:
    def __init__(self, r):
        self.r = r


main_rect = Rectangle(5, 4)
print(main_rect.area())
main_circle = Circle(2)

