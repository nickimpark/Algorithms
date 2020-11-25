def even(n):
        if n%2==0:
            return 1
        return 0

def qpow(a, n):
    b=1
    if not even(n):
        b=a
        n-=1
    while n!=1:
        a*=a
        n/=2
    a*=b
    return a

"""
a, n = (int(i) for i in input().split())
print(qpow(a,n))
"""
