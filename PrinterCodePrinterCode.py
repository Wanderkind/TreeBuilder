l=[]
while 1:
    i=input()
    if i!='':
        for j in i:
            l.append(ord(j))
        l.append(10)
    else:
        del l[-1]
        break
print(f"print(''.join([*map(chr,{l})]))")
