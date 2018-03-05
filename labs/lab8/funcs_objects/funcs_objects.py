import math


def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance


def circles_overlap(c1, c2):
    sum_radii = c1.radius + c2.radius
    center_distance = distance(c1.center, c2.center)
    return center_distance < sum_radii


