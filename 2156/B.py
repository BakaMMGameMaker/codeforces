t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))
    ms = input()  # machines
    qs = list(map(int, input().split()))  # querys
    if ms.count("B") == 0:
        for _q in qs:
            print(_q)
        continue
    if ms.count("A") == 0:
        for _q in qs:
            print(len(bin(_q)[2:]))
        continue

    # 计算一个最大阈值，使得其经过一个完整周期刚好不死，即得到 1
    thre = 1
    for machine in reversed(ms):
        if machine == "A":
            thre += 1
        else:
            thre *= 3
            thre -= 1

    def go(x: int) -> int:
        for machine in ms:
            if machine == "A":
                x -= 1
            else:
                x //= 2
        return x

    for _q in qs:
        ans = 0

        while _q >= thre:
            _q = go(_q)
            ans += n

        while _q:
            for machine in ms:
                if machine == "A":
                    _q -= 1
                else:
                    _q //= 2
                ans += 1
                if not _q:
                    break
        print(ans)
