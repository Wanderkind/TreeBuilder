key=input('input key > ').replace(' ','')
l=list(input('input plaintext > ').replace(' ',''))
k=[]
for i in key:
    if i not in k:
        k.append(i)
for i in range(26):
    q=chr(97+i)
    if q not in k:
        k.append(q)
k.remove('q')
K=[]
for i in range(5):
    K.append(k[5*i:5*i+5])
d={}
for i in range(5):
    for j in range(5):
        d[K[i][j]]=[i,j]
z=0
while 1:
    try:
        a,b=l[z],l[z+1]
        if a==b:
            l.insert(z+1,'x')
            continue
    except IndexError:
        l.append('x')
        continue
    R,C=d[a];r,c=d[b]
    if R==r:
        l[z],l[z+1]=K[R][(C+1)%5],K[r][(c+1)%5]
    elif C==c:
        l[z],l[z+1]=K[(R+1)%5][C],K[(r+1)%5][c]
    else:
        l[z],l[z+1]=K[R][c],K[r][C]
    z+=2
    if z==len(l):
        break
E=''.join(l).upper()
print(E)
