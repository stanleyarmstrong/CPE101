def poly_add2(l1, l2):
    l3 = list(l1)
    l3[0] += l2[0]
    l3[1] += l2[1]
    l3[2] += l2[2]
    return l3


def poly_mult2(l1 , l2):
    l3 = []
    l3.append(l1[0] * l2[0])
    l3.append((l1[0] * l2[1]) + (l1[1] + l2[0]))
    l3.append((l1[0] * l2[2]) + (l1[1] * l2[1]) + (l1[2] * l2[0]))
    l3.append((l1[1] * l2[2]) + (l1[2] * l2[1]))
    l3.append(l1[2] * l2[2])
    return l3
