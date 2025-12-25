def run():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    if n == 1:
        if a[0] == x:
            print("yes")
        else:
            print("no")
        return
    # 一旦列表中出现 x，那么整个列表都能收敛到 x
    # 问题转化为让列表出现 x
    # 只要相邻数对中，所形成的区间可包含 x，则可以出现 x
    for i in range(n - 1):
        if a[i] <= x <= a[i + 1]:
            print("yes")
            return
        if a[i] >= x >= a[i + 1]:
            print("yes")
            return
    print("no")


t = int(input())
for _ in range(t):
    run()
