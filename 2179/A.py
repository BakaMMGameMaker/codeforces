t = int(input())
for _ in range(t):
    k, x = list(map(int, input().split()))
    # 将字符串按照 mod x 分组
    # 每组的地位是等价的，所以只需要考虑其中一组
    # 这一组中最多只能出现 k 个字符
    # 所以 s 的最大长度就是 k * x
    # 第一个爆炸的就是 k * x + 1
    print(k * x + 1)
