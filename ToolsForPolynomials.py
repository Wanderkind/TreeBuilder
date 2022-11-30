
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

def polyprint(a):
    for i in a:
        print('( ', end = '')
        l=len(i)
        for j in range(l):
            print(f'{i[j]} ', end = '')
        print(')', end = ' ')
    print()

def polyp(a):
    
    ans = ''
    
    for i in a:
        ans += '( '
        l=len(i)
        for j in range(l):
            ans += f'{i[j]} '
        ans += ') '
    
    return ans

def yas(a, n):
    for i in a:
        s = synthdiv(i)
        if len(s) == n:
            S = polyp(s)
            w = S.split()
            t = [w[4*i+2] for i in range(n)]
            for j in t:
                print((int(j)>=0)*' '+j, end = ' ')
            print()
    print()
