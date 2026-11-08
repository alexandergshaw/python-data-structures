class Shape:
    def __init__(self, color):
        pass

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, width, height):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, color, a, b, c):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass


class Square(Rectangle):
    def __init__(self, color, side):
        pass


def largest_shape(shapes):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
