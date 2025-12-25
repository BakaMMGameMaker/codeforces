t = int(input())
for _ in range(t):
    """
    假设我们从 1 开始构造 a
    假设现在构造出了 1112222
    b7 = 10
    如果我们在后面放 3 （全新元素），那么对应 b8 就是 b7 + 7 + 1 = 18，每一项加 1 即可

    如果我们在后面放当前序列的最后一个元素，那么对应 b8 = b7，因为每一项都没有变化

    如果我们在后面放当前序列出现过但不等于末尾元素的元素，b8 = b7 + 末尾元素连续出现的次数 + 1 = 15
    这是因为除了末尾的元素，其它的元素都已经和新加的元素见过面了，对 b 的贡献不会发生改变

    根据以上结论，我们可以知道如果 b[i + 1] - b[i] = i + 1，说明要添加 max(a) + 1
    如果 b[i + 1] = b[i]，说明要添加 a[-1]
    否则，m = b[i + 1] - b[i]，添加 a[-m] 位置的元素
    """
    n = int(input())
    b = list(map(int, input().split()))
    a = [1]  # b1 一定是 1
    mx = 1
    for i in range(1, n):
        bi = b[i]
        bprev = b[i - 1]
        m = b[i] - b[i - 1]
        if m == i + 1:
            a.append(mx + 1)
            mx += 1
            continue
        if m == 0:
            a.append(a[-1])
            continue
        a.append(a[-m])
    print(*a)
