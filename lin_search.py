def lin_search(a,x):
    for i in range(len(a)):
        if a[i] == x:
            return i

"""
a = [int(i) for i in input().split()]
x = int(input())
index = lin_search(a, x)
print(index, a[index])
"""
