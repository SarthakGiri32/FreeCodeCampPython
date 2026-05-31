from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        shape_str = ""
        for i in range(self.height):
            for j in range(self.width):
                shape_str += "*"
            shape_str += "\n"

        return shape_str

    def get_amount_inside(self, shape: Rectangle):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.width = new_height
        self.height = new_height

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    def __str__(self):
        return f"Square(side={self.width})"


def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))


if __name__ == "__main__":
    main()
