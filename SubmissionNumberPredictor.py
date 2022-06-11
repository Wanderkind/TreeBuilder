import numpy as np
import matplotlib.pyplot as plt
X=[]
Y=[]
while 1:
    i=input()
    if i=='':break
    y,m,s=map(int,i.split())
    x=60*m+s
    X.append(x)
    Y.append(y)
plt.plot(X,Y,'b.')
plt.show()

'''
input()
z=input()
input()
for i in range(len(z)):
    if z[i:i+5]=='>4444':
        y=int(z[i+5:i+9])
        j=0
        while 1:
            if z[i+j:i+j+10]=='2022-06-12':
                h=(int(z[i+j+12])-3)*60
                m=int(z[i+j+14:i+j+16])
                s=int(z[i+j+17:i+j+19])
                print(y,h+m,s)
                break
            else:
                j+=1
'''
