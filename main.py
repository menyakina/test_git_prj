class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def get_height(self):
        return self.a

    def get_width(self):
        return self.b

    def perimetr(self):
        return self.a * 2 + self.b * 2
    def set_heigt(self, a):
        self.a = a

        def set_width(self, b):
            self.b = b


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r**2


main_rect = Rectangle(5, 4)
print(main_rect.area())
print(main_rect.perimetr())
main_circle = Circle(7)
print(main_circle.area())

