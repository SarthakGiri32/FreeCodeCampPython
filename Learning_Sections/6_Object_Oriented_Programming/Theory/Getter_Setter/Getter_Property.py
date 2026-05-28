class Circle:
    def __init__(self, radius):
        self._radius = radius
        # a convention in python to denote an attribute as private (not the actual syntax for private attributes)

    @property
    def radius(self):  # A getter to get the radius
        return self._radius

    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)


my_circle = Circle(3)

print(my_circle.radius)  # 3
print(my_circle.area)  # 28.26