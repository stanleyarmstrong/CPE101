from utility import epsilon_equal

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        check_x = epsilon_equal(self.x, other.x)
        check_y = epsilon_equal(self.y, other.y)
        return check_x and check_y


class Circle:

    def __init__(self, center, radius):
        self.radius = radius
        self.center = center

    def __eq__(self, other):
        check_center_x = epsilon_equal(self.center.x, other.center.x)
        check_center_y = epsilon_equal(self.center.y, other.center.y)
        check_radius = epsilon_equal(self.radius, other.radius)
        return check_center_x and check_center_y and check_radius
