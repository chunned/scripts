# Let a and b be positive integers
# Extended Euclidean algorithm is an efficient way to find integers u, v such that
# au + bv = gcd(a, b)
def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_s, old_t


p = 26513
q = 32321
print(extended_gcd(p, q))

