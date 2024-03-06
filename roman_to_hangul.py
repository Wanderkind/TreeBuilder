solo = {
    'a': 12609, 'A': 12609, # ㅁ
    'b': 12640, 'B': 12640, # ㅠ
    'c': 12618, 'C': 12618, # ㅊ
    'd': 12615, 'D': 12615, # ㅇ
    'e': 12599,             # ㄷ
    'E': 12600,             # ㄸ
    'f': 12601, 'F': 12601, # ㄹ
    'g': 12622, 'G': 12622, # ㅎ
    'h': 12631, 'H': 12631, # ㅗ
    'i': 12625, 'I': 12625, # ㅑ
    'j': 12627, 'J': 12627, # ㅓ
    'k': 12623, 'K': 12623, # ㅏ
    'l': 12643, 'L': 12643, # ㅣ
    'm': 12641, 'M': 12641, # ㅡ
    'n': 12636, 'N': 12636, # ㅜ
    'o': 12624,             # ㅐ
    'O': 12626,             # ㅒ
    'p': 12628,             # ㅔ
    'P': 12630,             # ㅖ
    'q': 12610,             # ㅂ
    'Q': 12611,             # ㅃ
    'r': 12593,             # ㄱ
    'R': 12594,             # ㄲ
    's': 12596, 'S': 12596, # ㄴ
    't': 12613,             # ㅅ
    'T': 12614,             # ㅆ
    'u': 12629, 'U': 12629, # ㅕ
    'v': 12621, 'V': 12621, # ㅍ
    'w': 12616,             # ㅈ
    'W': 12617,             # ㅉ
    'x': 12620, 'X': 12620, # ㅍ
    'y': 12635, 'Y': 12635, # ㅛ
    'z': 12619, 'Z': 12619  # ㅋ
}

initial = {
	'r': 0, 'R': 1,   # ㄱ, ㄲ
	's': 2, 'S': 2,   # ㄴ
	'e': 3, 'E': 4,   # ㄷ, ㄸ
	'f': 5, 'F': 5,   # ㄹ
	'a': 6, 'A': 6,   # ㅁ
	'q': 7, 'Q': 8,   # ㅂ, ㅃ
	't': 9, 'T': 10,  # ㅅ, ㅆ
	'd': 11, 'D': 11, # ㅇ
	'w': 12, 'W': 13, # ㅈ, ㅉ
	'c': 14, 'C': 14, # ㅊ
	'z': 15, 'Z': 15, # ㅋ
	'x': 16, 'X': 16, # ㅌ
	'v': 17, 'V': 17, # ㅍ
	'g': 18, 'G': 18  # ㅎ
}

medial = {
	'k': 0,  'K': 0,  # ㅏ
	'o': 1,           # ㅐ
    'i': 2,  'I': 2,  # ㅑ
    'O': 3,           # ㅒ
    'j': 4,  'J': 4,  # ㅓ
    'p': 5,           # ㅔ
    'u': 6,  'U': 6,  # ㅕ
    'P': 7,           # ㅖ
    'h': 8,  'H': 8,  # ㅗ
    #  9 -> ㅘ, 10 -> ㅙ, 11 -> ㅚ
    'y': 12, 'Y': 12, # ㅛ
    'n': 13, 'N': 13, # ㅜ
    # 14 -> ㅝ, 15 -> ㅞ, 16 -> ㅟ
    'b': 17, 'B': 17, # ㅠ
    'm': 18, 'M': 18, # ㅡ
    # 19 -> ㅢ
    'l': 20, 'L': 20  # ㅣ
}

final = {
    'r': 1,           # ㄱ
    'R': 2,           # ㄲ
    # 3 -> ㄳ
    's': 4, 'S': 4,   # ㄴ
    # 5 -> ㄵ, 6 -> ㄶ
    'e': 7, 'E': 7,   # ㄷ
    'f': 8, 'F': 8,   # ㄹ
    # 9 10 11 12 13 14 15
    'a': 16, 'A': 16, # ㅁ
    'q': 17, 'Q': 17, # ㅂ
    # 18 -> ㅄ
    't': 19,          # ㅅ
    'T': 20,          # ㅆ
    'd': 21, 'D': 21, # ㅇ
    'w': 22, 'W': 22, # ㅈ
    'c': 23, 'C': 23, # ㅊ
    'z': 24, 'Z': 24, # ㅋ
    'x': 25, 'X': 25, # ㅌ
    'v': 26, 'V': 26, # ㅍ
    'g': 27, 'G': 27  # ㅎ
}


f_to_i = {
    1: 0, 2: 1, 4: 2, 7: 3, 8: 5, 16: 6, 17: 7, 19: 9, 20: 10,
    21: 11, 22: 12, 23: 14, 24: 15, 25: 16, 26: 17, 27: 18
}

def trans(f):
    try:
        return f_to_i[f]
    except KeyError:
        assert False

t = {
    0: 0, 1: 1, 2: 3, 3: 6, 4: 7, 5: 8, 6: 16, 7: 17, 8: 18, 9: 20,
    10: 21, 11: 22, 12: 23, 13: 24, 14: 25, 15: 26, 16: 27, 17: 28, 18: 29
}

def trans_2(i):
    try:
        return t[i]
    except KeyError:
        assert False

dubconst = {
    (1, 19): 3,
    (4, 22): 5,
    (4, 27): 6,
    (8,  1): 9,
    (8, 16): 10,
    (8, 17): 11,
    (8, 19): 12,
    (8, 25): 13,
    (8, 26): 14,
    (8, 27): 15,
    (17, 19): 18
}

def dc(x, y):
    try:
        return dubconst[(x, y)]
    except KeyError:
        assert False

construct = lambda I, M, F: 44032 + 588*I + 28*M + F

I, M, F, S = -1, -1, -1, -1
flsh = True

def roman_to_hangul(text):
    res = []
    global I, M, F, S, flsh
    flsh = True
    def remain():
        global I, M, F, S, flsh
        flsh = False
        if I == -1:
            pass
        elif M == -1:
            res.append(chr(12593 + trans_2(I)))
        elif F == -1:
            res.append(chr(construct(I, M, 0)))
        elif S == -1:
            res.append(chr(construct(I, M, F)))
        else:
            try:
                res.append(chr(construct(I, M, dubconst[(F, S)])))
            except KeyError:
                try:
                    X = initial[S]
                    res.append(chr(construct(I, M, F)))
                    res.append(chr(12593 + X))
                except KeyError:
                    res.append(chr(construct(I, M, 0)))
                    res.append(chr(construct(trans(F), S, 0)))
        I, M, F, S = -1, -1, -1, -1
    for char in text:
        o = ord(char)
        if o < 65 or 90 < o < 97 or 122 < o:
            remain()
            res.append(char)
            continue
        flsh = True
        if I == -1:
            try:
                I = initial[char]
            except KeyError:
                res.append(chr(solo[char]))
        elif M == -1:
            try:
                M = medial[char]
            except KeyError:
                res.append(chr(12593 + trans_2(I)))
                res.append(chr(solo[char]))
                I = -1
        elif F == -1:
            try:
                F = final[char]
            except KeyError:
                if M == 8:
                    m = medial[char]
                    if m == 0:
                        M = 9
                    elif m == 1:
                        M = 10
                    elif m == 20:
                        M = 11
                    else:
                        res.append(chr(construct(I, M, 0)))
                        res.append(chr(solo[char]))
                        I, M = -1, -1
                elif M == 13:
                    m = medial[char]
                    if m == 4:
                        M = 14
                    elif m == 5:
                        M = 15
                    elif m == 20:
                        M = 16
                    else:
                        res.append(chr(construct(I, M, 0)))
                        res.append(chr(solo[char]))
                        I, M = -1, -1
                elif M == 18:
                    m = medial[char]
                    if m == 20:
                        M = 19
                    else:
                        res.append(chr(construct(I, M, 0)))
                        res.append(chr(solo[char]))
                        I, M = -1, -1
                else:
                    res.append(chr(construct(I, M, 0)))
                    res.append(chr(solo[char]))
                    I, M = -1, -1
        elif S == -1:
            try:
                S = final[char]
                if F == 1:
                    if S != 19:
                        res.append(chr(construct(I, M, F)))
                        I, M, F = trans(S), -1, -1
                        S = -1
                elif F == 4:
                    if S not in (22, 27):
                        res.append(chr(construct(I, M, F)))
                        I, M, F = trans(S), -1, -1
                        S = -1
                elif F == 8:
                    if S not in (1, 16, 17, 19, 25, 26, 27):
                        res.append(chr(construct(I, M, F)))
                        I, M, F = trans(S), -1, -1
                        S = -1
                elif F == 17:
                    if S != 19:
                        res.append(chr(construct(I, M, F)))
                        I, M, F = trans(S), -1, -1
                        S = -1
                else:
                    res.append(chr(construct(I, M, F)))
                    I, M, F = trans(S), -1, -1
                    S = -1
            except KeyError:
                res.append(chr(construct(I, M, 0)))
                I, M = trans(F), medial[char]
                F, S = -1, -1
        else:
            try:
                X = initial[char]
                res.append(chr(construct(I, M, dc(F, S))))
                I, M, F, S = X, -1, -1, -1
            except KeyError:
                res.append(chr(construct(I, M, F)))
                I, M = trans(S), medial[char]
                F, S = -1, -1
    if flsh:
        remain()
    return ''.join(res)
