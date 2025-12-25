t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n == 1:
        print(1)
        continue
    lmx = rmx = 0
    if s[0] == "<":
        lmx = 1
        while lmx < n and s[lmx] == "<":
            lmx += 1
    if s[n - 1] == ">":
        rmx = 1
        while rmx < n and s[n - 1 - rmx] == ">":
            rmx += 1
    # 往哪走都会漂流到岸上
    if lmx + rmx == n - 1:
        print(max(lmx, rmx) + 1)
        continue
    # 只要左右不相接，就可以在中间无限游荡
    if lmx + rmx < n:
        print(-1)
    else:
        print(max(lmx, rmx))
