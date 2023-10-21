def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True

def is_prime(n): # n > 1, otherwise inf loop
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    return not any(_try_composite(a, d, n, s) for a in (31, 73))
    """
    (31, 73)   for n < 9_080_191
    (2, 3, 5)  for n < 25_326_001
    (2, 7, 61) for n < 4_759_123_141
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41) for n < 2**64
    """
