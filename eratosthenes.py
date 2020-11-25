def eratosthenes(n):
    a = []
    num_bool = [True] * (n + 1)
    num_bool[0], num_bool[1] = False, False
    for i in range(2, n):
        for j in range(2 * i, n, i):
            num_bool[j] = False
    for i in range(n):
        if num_bool[i]:
            a.append(i)
    return a
"""
n = int(input())
print(*eratosthenes(n))
"""
