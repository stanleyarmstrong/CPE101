def square_all(l1):
    l2 = [x**2 for x in l1]
    return l2


def add_n_all(n, l1):
    for i in range(len(l1)):
        l1[i] += n
    return l1


def even_or_odd_all(l1):
    i = 0
    l2 = []
    while i < len(l1):
        if l1[i] % 2 == 0:
            l2.append(True)
        else:
            l2.append(False)
        i += 1
    return l2
