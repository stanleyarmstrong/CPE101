import math
from objects import *


def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance


def distance_all(l1):
    origin = Point(0, 0)
    l2 = [distance(origin, point) for point in l1]
    return l2


def are_in_first_quadrant(l1):
    l2 = [point for point in l1 if (point.x > 0) and (point.y > 0)]
    return l2
