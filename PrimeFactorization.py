from collections import Counter as C
def fc(n):
    l = []
    i = 2
    while n > 1:
        if n % i:
            i += 1 if i == 2 else 2
        else:
            l.append(i)
            n //= i
    c=C(l)
    #return [(i, c[i]) for i in c]
    return c
