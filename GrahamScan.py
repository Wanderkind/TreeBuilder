# credits to https://gist.github.com/arthur-e/5cf52962341310f438e96c1f3c3398b8

from functools import reduce as R

Q=lambda a:(a>0)-(a<0)
T=lambda p,q,r:Q((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
def _L(H,r):
    while len(H)>1 and T(H[-2],H[-1], r)==-1:H.pop() # <1 to exclude colinear points
    if not len(H) or H[-1]!=r:H.append(r)
    return H
def c(P):
    P.sort()
    l=R(_L,P,[])
    u=R(_L,P[::-1],[])
    return l.extend(u[i] for i in range(1,len(u)-1)) or l
