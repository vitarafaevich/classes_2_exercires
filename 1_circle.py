class Circle:
    """
    Class representing a circle
    """
    all_circles = []
    pi = 3.1415

    def __init__(self, radius=1):
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        """
        Method area(): counting the area of the circle
        :return: the area of the circle
        """
        return Circle.pi * self.radius ** 2

    def __repr__(self):
        return str(self.radius)

    @staticmethod
    def total_area():
        """
        Method total_area(): counting the area of the circle
        :return: the summarized area of the circles
        """
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total




c1 = Circle()
c2 = Circle(7)
c3 = Circle(5)
print(c2.area())
print(c3)
print(Circle.pi)
print(Circle.all_circles)
print(Circle.total_area())
print(len(c3.__class__.all_circles))

