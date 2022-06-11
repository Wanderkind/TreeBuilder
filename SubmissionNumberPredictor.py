import numpy as np
import matplotlib.pyplot as plt
X=[]
Y=[]
input()
z=input()
input()
for i in range(len(z)-22):
    if z[i:i+5]=='>4444':
        y=int(z[i+5:i+9])
        j=0
        while j<2*10**4:
            if z[i+j:i+j+10]=='2022-06-12':
                h=(int(z[i+j+12])-4)*60
                m=int(z[i+j+14:i+j+16])-40
                s=int(z[i+j+17:i+j+19])
                print(y,h+m,s)
                X.append((h+m)+s/60)
                Y.append(y)
                break
            else:
                j+=1
plt.plot(X,Y,'b.')
plt.show()
