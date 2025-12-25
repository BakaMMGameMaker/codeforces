t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # Case1: 有 1
    if a[0] == 1:
        print(1, a[1])
        continue
    # Case2: 有两个以上偶数
    e: list[int] = []
    for num in a:
        if num & 1 == 0:
            e.append(num)
            if len(e) == 2:
                print(f"{e[0]} {e[1]}")
                break
    if len(e) == 2:
        continue
    # Case3: 依赖奇数
    # 如果元素个数比较少，那么相邻奇数可能差很多倍，暴力枚举
    if n <= 32:
        found = 0
        for i in range(n - 1):
            p = a[i]
            for j in range(i + 1, n):
                q = a[j]
                if not (q % p) & 1:
                    print(f"{p} {q}")
                    found = 1
                    break
            if found:
                break
        if not found:
            print(-1)
    # 如果元素个数很多，同时又只有一个以下偶数，那么一定存在
    # 相邻奇数使得后面的奇数小于前面的两倍（否则超范围）
    # 在这种情况下，取模的结果就是两个奇数相见，结果一定是偶数
    else:
        found = 0
        for i in range(n - 1):
            p, q = a[i], a[i + 1]
            if not (q % p) & 1:
                print(f"{p} {q}")
                found = 1
                break
        if not found:
            print(-1)
