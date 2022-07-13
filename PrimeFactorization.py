def fc(n):
    l=[]
    i=2
    while n>1:
        if N%i==0:l.append(i);n/=i
        else:i+=1
    return l
