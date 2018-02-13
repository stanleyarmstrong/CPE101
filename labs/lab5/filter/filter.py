def are_positive(l1):
    l2 = []
    for i in range(len(l1)):
        if l1[i] >= 0:
            l2.append(l1[i])
    return l2


def are_greater_than_n(n, l1):
    l2 = []
    for i in range(len(l1)):
        if l1[i] > n:
            l2.append(l1[i])
    return l2


def are_divisible_by_n(n, l1):
    l2 = []
    for i in range(len(l1)):
        if l1[i] % n == 0:
            l2.append(l1[i])
    return l2
