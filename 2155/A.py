t = int(input())
for _ in range(t):
    n = int(input())
    # 已知一个 n 只会对应一个结果
    # 淘汰一组至少需要两场比赛
    # 需要淘汰 n - 1 组来得到冠军
    print(n - 1 + n - 1)
