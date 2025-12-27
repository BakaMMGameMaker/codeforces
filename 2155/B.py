t = int(input())
for _ in range(t):
    """
    只要不是只剩下一个空位，就有救
    UUUU
    UUUD
    RRRL
    """
    n, k = list(map(int, input().split()))
    n2 = n * n
    if k == n2 - 1:
        print("no")
        continue
    # 从左到右，从上到下填充 k 个 U
    # 最后一个 k 所在的行索引: ki = (k - 1) // n
    # ki, kj 是 ki * n + kj + 1 个出口
    ki = (k - 1) // n  # 最后一个出口行索引
    kj = k - 1 - ki * n  # 最后一个出口列索引
    grid: list[list[str]] = [[] for _ in range(n)]
    # 有 ki 行全是 U
    for i in range(ki):
        grid[i] = ["U" for _ in range(n)]
    grid[ki] = ["U" for _ in range(kj + 1)]
    # 如果末尾只剩下一个位置，由于至少剩下两个非出口，因此一定有下一行，可以安全塞 D
    rest = n - kj - 1
    if rest == 1:
        grid[ki].append("D")
    elif rest > 1:
        for _ in range(kj + 1, n - 1):
            grid[ki].append("R")
        grid[ki].append("L")
    # 剩下行都是 RR..L
    for i in range(ki + 1, n):
        grid[i] = ["R" for _ in range(n - 1)]
        grid[i].append("L")
    print("yes")
    for line in grid:
        print("".join(line))
