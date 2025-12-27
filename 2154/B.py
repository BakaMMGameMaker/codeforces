t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # 显然，让山峰更高是免费的，而且没有任何坏处
    curmax = 0
    for idx, num in enumerate(a):
        if num > curmax:
            curmax = num
        if idx & 1:
            a[idx] = curmax
    # 现在只需要把应当是山谷的位置拉低即可
    # 由于左侧的山峰不可能高于右侧的山峰，因此只需要低于左侧的山峰即可
    res = 0
    for i in range(2, n, 2):
        if a[i] >= a[i - 1]:
            res += a[i] - a[i - 1] + 1
    # 特别判断第一个位置，因为第一个位置左侧没有山峰
    if a[0] >= a[1]:
        res += a[0] - a[1] + 1
    print(res)
