t = int(input())
for _ in range(t):
    # n: 区域数量
    # x: A 党支持人数
    # y: B 党支持人数
    # si = 0, ai > bi
    # si = 1, ai < bi
    # ai + bi >= pi
    # 如果 si == 0，则 ai >= pi // 2 + 1
    # 如果 si == 1，则 bi >= pi // 2 + 1
    # sigma ai = x, sigma bi = y
    n, x, y = list(map(int, input().split()))
    s = input()
    p = list(map(int, input().split()))
    a: list[int] = []
    b: list[int] = []
    suma = sumb = 0
    total_need = 0
    for i in range(n):
        pi = p[i]
        mn = pi // 2 + 1
        total_need = pi - mn
        si = s[i]
        if si == "0":
            a.append(mn)
            suma += mn
            b.append(0)
        else:
            a.append(0)
            b.append(mn)
            sumb += mn
    if suma > x or sumb > y:
        print("no")
        continue
    if total_need > (x - suma) + (y - sumb):
        print("no")
        continue
    # 不会喵
    print("yes")
