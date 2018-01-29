def max_101(x,y):
    if(x > y):
        return x
    else:
        return y
def max_of_three( x , y , z ):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z
def repeated_max_of_three():
    while True:
        num1 = input('Number 1:')
        if(num1 == 'q'):
            break
        num2 = input('Number 2:')
        if(num2 == 'q'):
            break
        num3 = input('Number 3:')
        if(num3 == 'q'):
            break
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        print(max_of_three(num1, num2, num3))
