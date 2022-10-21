
import sys
input=lambda:sys.stdin.readline().strip()

def f(w):
    
    w=list(w)
    
    left=[]
    right=[]
    for i in range(len(w)):
        if w[i]=='(':
            left.append(i)
        if w[i]==')':
            right.append(i)
    
    if right and left and right[0]<left[0]:
        del right[0]
    
    dlt=[]
    for i in range(len(left)):
        if not(i+1!=len(left) and left[i+1]<right[i]):
            dlt+=[*range(left[i]+1,right[i])]
        else:
            dlt+=[*range(left[i]+1,right[i+1])]
    
    dlt=sorted(list(set(dlt)))
    for i in dlt[::-1]:
        del w[i]
    
    w=''.join(w).replace('()','(          )')
    return w

L=[]
while 1:
    w=input()
    if w=='#####':break
    L.append(f(w))

print('\n\n============== Blanked reuslt ==============\n\n')
for i in L:
    print(i)
