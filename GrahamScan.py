# credits to https://gist.github.com/arthur-e/5cf52962341310f438e96c1f3c3398b8

from functools import reduce as R

Q=lambda a:(a>0)-(a<0)
T=lambda p,q,r:Q((q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1]))
def L(H,r):
    while len(H)>1 and T(H[-2],H[-1],r)<1:H.pop() # ==-1 to include colinear points
    if not len(H) or H[-1]!=r:H.append(r)
    return H
def c(P):
    P.sort();l,u=R(L,P,[]),R(L,P[::-1],[])
    return l+[u[i] for i in range(1,len(u)-1)] or l

# C=c([[*map(int,input().split())]for _ in range(int(input()))])
