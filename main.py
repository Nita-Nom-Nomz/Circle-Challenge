import math


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius


radius = float(input("Enter the radius of the circle:\n> "))
circle = Circle(radius)

while True:
    print("Diameter:", int(circle.calculate_diameter()))
    print("Circumference:", circle.calculate_circumference())
    print("Area:", circle.calculate_area())

    choice = input("Would you like your circle to grow? (y/n):\n> ").lower()
    if choice == 'y':
        circle.grow()
    elif choice == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
