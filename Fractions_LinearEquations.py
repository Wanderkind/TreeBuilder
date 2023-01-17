from math import gcd

def fmul(p, q):
    a, b = p
    c, d = q
    u, v = a*c, b*d
    g = gcd(u, v)
    return [u//g, v//g]

def fadd(p, q):
    a, b = p
    c, d = q
    u, v = a*d+b*c, b*d
    g = gcd(u, v)
    return [u//g, v//g]

def dmul(k, d): # k is fraction, d is dict
    ans = {}
    for i in d:
        ans[i] = fmul(k, d[i])
    return ans

def dadd(d1, d2):
    ans = d2.copy()
    for i in d1:
        if i in d2:
            ans[i] = fadd(d1[i], d2[i])
        else:
            ans[i] = d1[i]
    return ans

def dexpress(d1, d2, key): # returns d1 with d2 disassembled. assumes that d1 has key of d2
    ans = d1.copy()
    coef = ans[key]
    del ans[key]
    return dadd(ans, dmul(coef, d2))

def dexpress_self(d1, key): # returns d1 with d1 disassembled. assumes that d1 has key of d1
    ans = d1.copy()
    coef = ans[key]
    del ans[key]
    return dmul(fadd([1,1], fmul([-1,1], coef))[::-1], ans)
