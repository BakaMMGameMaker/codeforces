t = int(input())
for _ in range(t):
    legs = int(input())
    if legs & 1:
        print(0)
        continue
    # 配置数 = 牛数量的可能性
    max_mow = legs // 4
    print(max_mow + 1)
