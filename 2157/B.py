t = int(input())
for _ in range(t):
    """
    最终覆盖的黑色区域和 '4' 与 '8' 的先后顺序无关
    如果 x y 离原点的水平或者数值距离超过了半径 n，则 NO
    如果 x y 位于由 '4' 形成的三角形区域中，则 NO
    否则 YES
    """
    n, x, y = list(map(int, input().split()))
    s = input()
    x = abs(x)
    y = abs(y)
    if x > n or y > n:
        print("no")
        continue
    # 右上角坐标为 n n
    # 每有 1 个 '4'，高度为 n 的位置就会尾随 1 个空白
    # 高度为 n - 1 的位置尾随的空白数量一定是上一层的 - 1
    # 坐标的高度为 y
    # 此高度处尾随的空白数量为 m = max(fours - (n - y), 0)
    # 此高度处最后一个黑色的坐标为 n - m
    # 如果 x > n - m，则 NO
    fours = s.count("4")
    m = max(fours - (n - y), 0)
    if x > n - m:
        print("no")
    else:
        print("yes")
