import random
L=[];A=[];i=0;s=[];X=[];Y=[]
while 1:
 I=input()
 if I!='0':L+=I.split()
 else:L+=['ㅋ'];break
while i<len(L):
 x=L[i];o=ord(x[0])
 if 44032<=o<=55203 or o<128:s+=[x]
 else:A+=[s];s=[x]
 i+=1
for i in range(1,len(A)):
 a=A[i];X+=[a.pop(0)];Y+=[' '.join(a)]
v=[i for i in range(len(X))]
########
random.shuffle(v)
########
print('\n\n')
for i in v:print(X[i])
print('\n\n')
for i in v:print(Y[i])
print('\n\n')
