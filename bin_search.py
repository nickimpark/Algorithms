def bin_search(a, x):
    i = 0
    j = len(a)-1
    m = j // 2
    while (a[m] != x) and i <= j:
        if x > a[m]:
            i = m + 1
        else:
            j = m - 1
        m = (i + j) // 2
    if i > j:
        return None
    else:
        return m

"""
a = sorted([int(i) for i in input().split()]) # Array must be sorted
print(*a)
x = int(input())
index = bin_search(a, x)
if index != None:
    print(index, a[index])
else:
    print('Not found')
"""
