def crt(a, n):     # Calculate Chinese Remainder Theorem for two arrays, a and n
    # a: array of arbitrary integers
    # n: array of pairwise co-prime integers that are used as the moduli
    if len(a) != len(n):
        raise ValueError("a and n must be the same length")
    # check that elements of n are pairwise co-prime
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if euclidean(n[i], n[j]) != 1:
                raise ValueError(f"{n[i]} and {n[j]} are not pairwise coprime.")

    # 1. calculate m
    # initialize m as 1, then multiply by each n
    m = 1
    for val in n:
        m *= val

    # 2. calculate M1, M2, ...
    M = [m // val for val in n]

    # 3. find inverse of each M
    y = [pow(M[i], -1, n[i]) for i in range(len(M))]  # inverses of each M
    # 4. find first positive solution x = a1 * M1 * y1 + a2 * M2 * y2 + a3 * M3 * y3
    x = 0
    for i in range(len(a)):
        x += a[i] * M[i] * y[i]

    return x % m


def euclidean(a, b): # compute gcd(a, b) using Euclidean Algorithm
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


crt([2, 3, 2], [3, 5, 7])
crt([2, 3, 5], [5, 11, 17])
