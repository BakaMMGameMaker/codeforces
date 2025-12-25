t = int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    r = "YES" if a == b == c == d else "NO"
    print(r)
