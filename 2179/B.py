t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # 如果 ai, ai+1, ai+2 是非严格递减或者非严格递增的，那么删除 ai+1 不会有任何帮助
    # 删除第一个元素或者最后一个元素一定可以带来增益，增益是 abs a[1] - a[0] 与 abs [-2] - [-1]
    # 查看删除每个元素可否带来增益，并求最大增益
    cur_cost = abs(a[1] - a[0])
    mx = abs(a[1] - a[0])  # 初始化为删除第一个元素带来的增益
    for i in range(1, n - 1):  # 遍历中间的元素，这些元素都有前和后
        r, s, t = a[i - 1], a[i], a[i + 1]
        # 计算原本的开销
        rs = abs(r - s)
        st = abs(s - t)
        cur_cost += st
        # s 还在的时候，这个窗口的开销
        p = rs + st
        # s 不在的时候，这个窗口的开销 = rt
        q = abs(r - t)
        # 删除 s 可以带来增益为 p - q
        mx = max(mx, p - q)
    mx = max(mx, abs(a[-2] - a[-1]))  # 删除最后一个元素
    print(cur_cost - mx)
