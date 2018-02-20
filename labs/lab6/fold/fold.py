def sum(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum


def index_of_smallest(l1):
    minimum = l1[0]
    for i in l1:
        if i <= minimum:
            minimum = i
    return minimum