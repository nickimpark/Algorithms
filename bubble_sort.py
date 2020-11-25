def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[i] > a[j]:
                t = a[i]
                a[i] = a[j]
                a[j] = t
    return a

"""
a = [int(i) for i in input().split()]
print(*bubble_sort(a))
"""
