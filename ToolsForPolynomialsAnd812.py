
from math import *
import sys
input=lambda:sys.stdin.readline().strip()
U=lambda:map(int,input().split())

def add(a, b):
    
    A = len(a)
    B = len(b)
    ans=[]
    
    if A<B:
        a = [0 for _ in range(B-A)]+a
    else:
        b = [0 for _ in range(A-B)]+b
    
    for i in range(max(A,B)):
        ans.append(a[-i-1]+b[-i-1])
    
    return ans[::-1]

def mul(a, b):
    
    A = len(a)
    B = len(b)
    ans=[0 for _ in range(A+B-1)]
    
    for i in range(B):
        q = b[-1-i]
        for j in range(A):
            ans[-1-i-j] += q*a[-1-j]
    
    return ans

def fin(a, b):
    
    A = len(a)
    B = len(b)
    ans=[]
    
    for i in range(A):
        c = [1]
        for _ in range(i):
            c = mul(c, b)
        ans = add(ans, [a[-1-i]*j for j in c])
    
    return ans

def shr(a, b): # assumes that b is monic
    
    A = len(a)
    B = len(b)
    ans=[]
    
    c = a[:B]
    for i in range(A-B+1):
        k = c[i]
        ans.append(k)
        c = add(c, [-k*j for j in b])
        if i<A-B:
            c += [a[B+i]]
    
    return ans

def rem(a, b): # assumes that b is monic
    
    A = len(a)
    B = len(b)
    
    c = a[:B]
    for i in range(A-B+1):
        c = add(c, [-c[i]*j for j in b])
        if i<A-B:
            c += [a[B+i]]
    
    for _ in range(A-1):
        if not c[0]:
            del c[0]
        else:
            break
    
    return c

def divides(a, b):
    return rem(a, b) == [0]

def dyn(a):
    return divides(fin(a, [1, 0, -2]), a)

from math import isqrt

def intfactors(n):
    
    factors = []
    q = isqrt(abs(n))
    
    for i in range(1, q):
        if not n%i:
            k = n//i
            factors += [i, k, -i, -k]
    
    return factors + [q, -q] + (q*q != n)*[n//q, -n//q]

def synthdiv(a):
    
    ans = []
    
    for h in range(len(a)):
        n = a[-1]
        if n:
            f = intfactors(n)
            for i in f:
                k = [1, -i]
                if divides(a, k):
                    ans.append([1, -i])
                    a = shr(a, k)
                    break
            if len(ans)==h:
                ans.sort()
                if len(a)>1:
                    ans.append(a)
                return ans
        else:
            ans.append([1, 0])
            a = a[:-1]
    
    return sorted(ans)

one=[
[1, -2]
,[1, 1]]
two=[
[1, -4, 4]
,[1, -1, -2]
,[1, 0, -4]
,[1, 0, -1]
,[1, 1, -1]
,[1, 2, 1]]
three=[
[1, -6, 12, -8]
,[1, -3, 0, 4]
,[1, -2, -4, 8]
,[1, -2, -1, 2]
,[1, -1, -3, 2]
,[1, 0, -4, 0]
,[1, 0, -3, -2]
,[1, 0, -3, 1]
,[1, 1, -4, -4]
,[1, 1, -2, -1]
,[1, 1, -1, -1]
,[1, 2, 0, -1]
,[1, 3, 3, 1]]
four=[
[1, -8, 24, -32, 16]
,[1, -5, 6, 4, -8]
,[1, -4, 0, 16, -16]
,[1, -4, 3, 4, -4]
,[1, -3, -1, 8, -4]
,[1, -2, -4, 8, 0]
,[1, -2, -3, 4, 4]
,[1, -2, -3, 7, -2]
,[1, -1, -6, 4, 8]
,[1, -1, -4, 3, 2]
,[1, -1, -4, 4, 1]
,[1, -1, -3, 1, 2]
,[1, 0, -8, 0, 16]
,[1, 0, -5, 0, 4]
,[1, 0, -4, -1, 2]
,[1, 0, -4, 0, 0]
,[1, 0, -4, 0, 3]
,[1, 0, -3, 0, 1]
,[1, 0, -2, 0, 1]
,[1, 1, -5, -4, 4]
,[1, 1, -4, -4, 0]
,[1, 1, -3, -5, -2]
,[1, 1, -3, -2, 1]
,[1, 1, -2, -1, 1]
,[1, 2, -3, -8, -4]
,[1, 2, -1, -3, -1]
,[1, 2, -1, -2, 1]
,[1, 2, 0, -2, -1]
,[1, 3, 2, -1, -1]
,[1, 4, 6, 4, 1]]

def polyprint(a):
    for i in a:
        print('( ', end = '')
        l=len(i)
        for j in range(l):
            print(f'{i[j]} ', end = '')
        print(')', end = ' ')
    print()


for i in four:
    s = synthdiv(i)
    polyprint(s)
    #print()

'''
while 1:
    a = [*U()]
    print(synthdiv(a))
'''
