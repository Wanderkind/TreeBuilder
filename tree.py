
def w(string):
    
    w = 0
    for x in range(len(string)):
        o = ord(str(string[x]))
        
        if 32 <= o < 161:
            w += 1
        
        else:
            w += 2
    
    return w

def sp(string):
    
    sp = ''
    for y in range(w(string)):
        sp += ' '
    
    return sp

DL = [None]
PL = [None]
CL = [[]]
OL = [None]
LL = []
ScL = []

cease = 'no'
count = 1
while cease == 'no':
    
    msg = f'Input parent # from 0 to {count - 1}, Input X to cease > '
    parentpre = input(msg)
    ScL.append(parentpre)
    
    if parentpre == 'X' or parentpre == 'x' or parentpre == 'ㅌ':
        cease = 'yes'
        break
    
    cease1 = 'no'
    while cease1 == 'no':
        
        if parentpre == '':
            parentpre = input(msg)
            ScL.append(parentpre)
            continue
        
        order = []
        for i in range(len(parentpre)):
            order.append(ord(parentpre[i]))
            
        if 48 <= min(order) and max(order) < 58:
            if 0 <= int(parentpre) < count:
                parent = int(parentpre)
                break
            
            else:
                parentpre = input(msg)
                ScL.append(parentpre)
                continue
        
        elif parentpre == 'X' or parentpre == 'x' or parentpre == 'ㅌ':
            cease1 == 'yes'
            break
        
        else:
            parentpre = input(msg)
            ScL.append(parentpre)
            continue
    
    PL.append(parent)
    CL.append([])
    CL[parent].append(count)
    OL.append(0)
    
    content = input('Input text > ')
    ScL.append(content)
    node = [count, content]
    
    if parent == 0:
        
        DL.append([len(LL), 0])
        
        Lt = []
        Lt.append(node)
        LL.append(Lt)
    
    else:
        
        l = DL[parent][0] + len(CL[parent]) - 1
        
        ancestor = parent
        while True:
            if len(CL[parent]) != 1:
                OL[ancestor] += 1
            ancestor = PL[ancestor]
            if ancestor == 0:
                break
        
        nonfirstnephew = 0
        for i in range(len(CL[parent]) - 1):
            nonfirstnephew += OL[CL[parent][i]]
        
        ln = l + nonfirstnephew
        
        if len(CL[parent]) == 1:
            
            DL.append([ln, DL[parent][1] + 1])
            
            LL[ln].append(node)
        
        else:
            
            DL.append([ln, DL[parent][1] + 1])
            for i in range(ln, len(LL)):
                for j in range(len(LL[i])):
                    if LL[i][j] != 'space':
                        DL[LL[i][j][0]][0] += 1
            
            LL.insert(ln, [])
            for i in range(DL[parent][1] + 1):
                LL[ln].append('space')
            LL[ln].append(node)
    
    count += 1
    
    LLps = []
    for i in range(len(LL)):
        lps = []
        for j in range(len(LL[i])):
            lps.append(LL[i][j])
        LLps.append(lps)
        
    for i in range(len(LLps)):
        for j in range(len(LLps[i]) - 1, 0, -1):
            
            if LLps[i][j - 1] != 'space':
                LLps[i].insert(j, '─')
            
            elif LLps[i][j] != 'space':
                LLps[i].insert(j, '└')
            
            else:
                LLps[i].insert(j, 'space')

    for i in range(len(LLps) - 1, 0, -1):
        SL = []
        for j in range(len(LLps[i - 1])):
            SL.append('space')
        LLps.insert(i, SL)

    for i in range(2, len(LLps), 2):
        
        j = 0
        while True:
            
            if LLps[i][j] == 'space':
                j += 2
                continue
             
            else:
                for k in range(j, len(LLps[i - 1])):
                    LLps[i - 1][k] = 'XXXXX'
                break

    l = []
    for i in range(len(LLps[- 1])):
        l.append('XXXXX')
    LLps.append(l)

    for i in range(len(LLps)):
        for j in range(len(LLps[i])):
            
            if LLps[i][j] == '─' or '└':
                
                k = i
                l = k
                while LLps[k][j] == 'space':
                    k += 1
                    if LLps[k][j] == '└':
                        break
                    
                    elif LLps[k][j] == 'XXXXX':
                        k = l
                        while LLps[k][j] == 'space':
                            k += 1
                            LLps[k][j] = 'XXXXX'
                            
                    else:
                        continue

    for i in range(1, len(LLps) - 2, 2):
        for j in range(len(LLps[i]) - 1):
            
            if LLps[i][j] == 'space' and LLps[i + 1][j] == 'XXXXX':
                LLps[i][j] = 'XXXXX'

    for i in range(0, len(LLps) - 3, 2):
        for j in range(1, len(LLps[i]) - 1, 2):
            
            if LLps[i][j] == '─' and LLps[i + 1][j] == 'space':
                LLps[i][j] = '┬'

    for i in range(0, len(LLps) - 3, 2):
        for j in range(1, len(LLps[i]) - 1, 2):
            
            if LLps[i][j] == '└' and len(LLps[i + 1]) >= j + 1 and len(LLps[i + 2]) >= j + 1:
                if LLps[i + 1][j] == 'space':
                    LLps[i][j] = '├'

    for i in range(1, len(LLps) - 2):
        for j in range(len(LLps[i]) - 1):
            
            if LLps[i][j] == 'space':
                LLps[i][j] = '│'

    for i in range(1, len(LLps), 2):
        
        while True:
            
            if LLps[i] != []:
                
                if LLps[i][-1] == 'XXXXX':
                    del LLps[i][-1]
                    continue
                    
                else:
                    break
             
            else:
                break

    del LLps[-1]
    
    for i in range(1, len(LLps)):
        for j in range(len(LLps[i]) - 1):
            if LLps[i][j] == 'XXXXX':
                LLps[i][j] = sp(str(LLps[i - 1][j]))
    
    print('')
    for i in range(len(LLps)):
        t = ''
        for j in range(len(LLps[i])):
            if isinstance(LLps[i][j], list):
                t += (str(LLps[i][j]) + ' ')
            else:
                t += (LLps[i][j] + ' ')
        print(t)
    print('')
    
for i in range(len(LL)):
    for j in range(len(LL[i]) - 1, 0, -1):
        
        if LL[i][j - 1] != 'space':
            LL[i].insert(j, '─')
        
        elif LL[i][j] != 'space':
            LL[i].insert(j, '└')
        
        else:
            LL[i].insert(j, 'space')

for i in range(len(LL) - 1, 0, -1):
    SL = []
    for j in range(len(LL[i - 1])):
        SL.append('space')
    LL.insert(i, SL)

for i in range(2, len(LL), 2):
    
    j = 0
    while True:
        
        if LL[i][j] == 'space':
            j += 2
            continue
         
        else:
            for k in range(j, len(LL[i - 1])):
                LL[i - 1][k] = 'XXXXX'
            break

l = []
for i in range(len(LL[- 1])):
    l.append('XXXXX')
LL.append(l)

for i in range(len(LL)):
    for j in range(len(LL[i])):
        
        if LL[i][j] == '─' or '└':
            
            k = i
            l = k
            while LL[k][j] == 'space':
                k += 1
                if LL[k][j] == '└':
                    break
                
                elif LL[k][j] == 'XXXXX':
                    k = l
                    while LL[k][j] == 'space':
                        k += 1
                        LL[k][j] = 'XXXXX'
                        
                else:
                    continue

for i in range(1, len(LL) - 2, 2):
    for j in range(len(LL[i]) - 1):
        
        if LL[i][j] == 'space' and LL[i + 1][j] == 'XXXXX':
            LL[i][j] = 'XXXXX'

for i in range(0, len(LL) - 3, 2):
    for j in range(1, len(LL[i]) - 1, 2):
        
        if LL[i][j] == '─' and LL[i + 1][j] == 'space':
            LL[i][j] = '┬'

for i in range(0, len(LL) - 3, 2):
    for j in range(1, len(LL[i]) - 1, 2):
        
        if LL[i][j] == '└' and len(LL[i + 1]) >= j + 1 and len(LL[i + 2]) >= j + 1:
            if LL[i + 1][j] == 'space':
                LL[i][j] = '├'

for i in range(1, len(LL) - 2):
    for j in range(len(LL[i]) - 1):
        
        if LL[i][j] == 'space':
            LL[i][j] = '│'

for i in range(1, len(LL), 2):
    
    while True:
        
        if LL[i] != []:
            
            if LL[i][-1] == 'XXXXX':
                del LL[i][-1]
                continue
                
            else:
                break
         
        else:
            break

del LL[-1]

for i in range(len(LL)):
    for j in range(len(LL[i])):
        if isinstance(LL[i][j], list):
            LL[i][j] = LL[i][j][1]

for i in range(1, len(LL)):
    for j in range(len(LL[i]) - 1):
        if LL[i][j] == 'XXXXX':
            LL[i][j] = sp(str(LL[i - 1][j]))

print('\n┌──────┬─────┬─────┬─────┐ ')
print('│      │ 9pt │ 10pt│ 11pt│ ')
print('├──────┼─────┼─────┼─────┤ ')
print('│ 기본 │ 94  │ 85  │ 77  │ ')
print('├──────┼─────┼─────┼─────┤ ')
print('│ 좁게1│ 106 │ 96  │ 87  │ ')
print('├──────┼─────┼─────┼─────┤ ')
print('│ 좁게2│ 119 │ 107 │ 97  │ ')
print('├──────┼─────┼─────┼─────┤ ')
print('│ 좁게 │ 119 │ 107 │ 97  │ ')
print('└──────┴─────┴─────┴─────┘ ')

while True:
    
    colpre = input('Input numer of columns > ')
    
    if colpre == '':
        colpre = input('Input numer of columns > ')
        continue
    
    order = []
    for i in range(len(colpre)):
        order.append(ord(colpre[i]))
    
    if 48 <= min(order) and max(order) < 58:
        col = int(colpre)
        break
    
    else:
        colpre = input('Input numer of columns per line > ')
        continue

for i in range(len(LL)):
    
    if all(x == ' ' for x in LL[i]):
        LL[i] = ''
    
    else:
        a = ''
        for j in range(len(LL[i])):
            a += str(LL[i][j])
            a += ' '
        LL[i] = a

Lprint = []
for i in range(len(LL)):
    
    a = ''
    broken = []
    for j in range(len(LL[i])):
        
        K = str(LL[i][j])
        a += K
        
        if K == '─' or K == '└' or K == '├' or K == '┬':
            broken.append(a + ' ')
        
        if w(a) >= col - 1:
            Lprint.append(a)
            
            if i != len(LL) - 1:
                
                if w(LL[i + 1]) != 0:
                    
                    if w(LL[i + 1]) == w(broken[-1]):
                        a = LL[i + 1]
                    
                    else:
                        a = sp(broken[-1])
                
                else:
                    a = sp(broken[-1])
            
            else:
                a = sp(broken[-1])
        
    Lprint.append(a)

for i in range(len(Lprint) - 1):
    Lprint[i + 1] = list(Lprint[i + 1])
    for j in range(len(Lprint[i])):
        if Lprint[i][j] == '│' or Lprint[i][j] == '┬':
            if Lprint[i + 1][j] == ' ':
                Lprint[i + 1][j] = '│'
                del Lprint[i + 1][j + 1]
    Lprint[i + 1] = ''.join(Lprint[i + 1])

print('\n▼▼▼▼▼▼▼▼▼▼\n')
for i in range(len(Lprint)):
    print(Lprint[i])
print('\n▲▲▲▲▲▲▲▲▲▲\n')

while True:
    
    ans = input('Print script? input P to print, Q to quit > ')
    if ans == 'P' or ans == 'p' or ans == 'ㅔ':
        
        print('')
        for i in range(len(ScL)):
            print(ScL[i])
        print('')
        break
    
    elif ans == 'Q' or ans == 'q' or ans == 'ㅂ':
        break
    
    else:
        continue
