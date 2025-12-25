t = int(input())
for _ in range(t):
    """
    分数过高就往死里减，一旦分数低于门槛，后面的比赛都能 rated，只要得分为 0 即可
    因此答案就是 n - 开头不可能为 rated 的比赛数量
    显然，开头不可能为 rated 的比赛就是超过了门槛但是为 div2 的比赛
    """
    r0, x, d, n = list(map(int, input().split()))
    s = input()
    norate = 0
    for i in range(n):
        if r0 < x:  # 已经到门槛以下
            break
        # 仍超过门槛 vvv
        div = s[i]
        if div == "2":  # unrated
            norate += 1
            continue
        # div == 1
        r0 -= d  # 能掉多少是多少
        r0 = max(r0, 0)  # 防止低于 0
    print(n - norate)
