from math import gcd

PRIMES = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    g = 0
    for v in a:
        g = gcd(g, v)
    for p in PRIMES:
        if g % p != 0:
            print(p)
            break
