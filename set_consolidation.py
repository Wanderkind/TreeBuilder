# functional

from functools import reduce

def consolidated(sets):
    def go(xs, s):
        if xs:
            h = xs[0]
            return go(xs[1:], h.union(s)) if h.intersection(s) else [h] + go(xs[1:], s)
        else:
            return [s]
    return reduce(go, sets, [])

# iterative

def consolidate(sets):
    setlist = [s for s in sets if s]
    for i, s1 in enumerate(setlist):
        if s1:
            for s2 in setlist[i+1:]:
                intersection = s1.intersection(s2)
                if intersection:
                    s2.update(s1)
                    s1.clear()
                    s1 = s2
    return [s for s in setlist if s]

# recursive

def conso(s):
    if len(s) < 2: return s
    r, b = [s[0]], conso(s[1:])
    for x in b:
        if r[0].intersection(x): r[0].update(x)
        else: r.append(x)
    return r
