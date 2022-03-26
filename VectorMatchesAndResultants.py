from math import log10
from itertools import permutations

def v(p,q):
    X,Y=p
    x,y=q
    return [x-X,y-Y]

def m(p,q):
    X,Y=p
    x,y=q
    return [X+x,Y+y]

for u in range(2,21):
    
    l=[]
    for i in range(2*u):
        l.append([1*(10**i),2*(10**i)])
    
    V=v(l[0],l[1])
    for i in range(1,u):
        V=m(V,v(l[2*i],l[2*i+1]))
    
    L=[]
    for I in permutations(l,2*u):
        
        i=[]
        for w in range(u):
            i.append([I[2*w],I[2*w+1]])
        
        R=v(i[0][0],i[0][1])
        for w in range(1,u):
            R=m(R,v(i[w][0],i[w][1]))
        
        if R==V:
            for z in i:
                for w in range(2):
                    z[w]=sum(z[w])
                z=sum(z)
            i.sort()
            if i not in L:
                L.append(i)
    
    print(f'For {2*u} points, there exist at most {len(L)} matches that make a particular resultant.')

# For 2*u points, there exist at most u! matches that make a particular resultant.
