import math


class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        return (f"A {self.color} shape with area {self.area():.2f} "
                f"and perimeter {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semi = self.perimeter() / 2
        return math.sqrt(semi * (semi - self.a) * (semi - self.b) * (semi - self.c))


class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)


def largest_shape(shapes):
    return max(shapes, key=lambda shape: shape.area())


def main():
    shapes = [Circle("red", 3), Rectangle("green", 4, 6),
              Triangle("blue", 3, 4, 5), Square("purple", 5)]
    for shape in shapes:
        print(shape.describe())
    print(f"Largest shape: {largest_shape(shapes).describe()}")


if __name__ == "__main__":
    main()
