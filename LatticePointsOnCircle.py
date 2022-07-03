from math import floor, sqrt
try: 
    long
except NameError: 
    long = int
 
def fac(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = 2 if n % 2 == 0 else 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return [q] + fac(n // q) if q <= maxq else [n]
 
def f(n):
    if n==1:
        return 4
    L=fac(n)
    S=set(L)
    z=1
    for i in S:
        c=L.count(i)
        if i%4==1:
            z*=(c+1)
        if i%4==3:
            if c%2==1:
                return 0
    return z*4

'''
while 1:
    print(f(int(input())))
'''
