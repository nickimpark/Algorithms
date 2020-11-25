def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a,b):
    return (a // gcd(a, b)) * b

"""    
a, b = (int(i) for i in input().split())
print('The greatest common factor: ', gcd(a, b))
print('The least common multiple : ', lcm(a, b))
"""