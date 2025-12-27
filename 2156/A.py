t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    # 想让 Hao 吃最多，只要让 m1 最大，同时 m2 = m1
    # 如果 n 是 3k，那么 m1 = m2 = m3 = k
    # 3k + 1: k k k+1
    # 3k + 2: k k k+2
    while n > 2:
        m1 = m2 = n // 3
        m3 = n - m1 - m2
        ans += m1
        n = m3
    print(ans)
