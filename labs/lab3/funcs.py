import math

def cube(x):
    return x**3
def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)
def f(x,y):
    if(x != 0):
        return ((3*x**2) + (4*y))/ (2 * x)
    else:
        return None
def is_positive(x):
    return x > 0
def both_positive(x ,y):
    return x > 0 and y > 0
