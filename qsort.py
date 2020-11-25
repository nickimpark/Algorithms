import random

def qsort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
    l = [i for i in a if i < q]
    e = [q] * a.count(q)
    r = [i for i in a if i > q]
    return qsort(l) + e + qsort(r) # [1]+[2, 2]+[3] = [1, 2, 2, 3] as example

"""
a = [int(i) for i in input().split()]
print(*qsort(a))
"""
