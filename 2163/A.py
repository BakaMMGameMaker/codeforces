def run():
    """
    souvlaki 通过提前重拍来让自己胜率最大
    重排后，至少应该满足以下性质
    souvlaki 对 a[even], a[even + 1] 的两个数的顺序有掌控权
    这意味着看上去这两个数字的大小关系没有所谓
    但是在这两个数字交换成非递减状态之后，souvlaki 必须确保
    新的 a[even + 1] <= a[even + 2]，不然 kalamaki 就可以不交换
    从而获得胜利。所以 souvlaki 操作之后，必须保证
    a[even] <= a[even + 1] <= a[even + 2]
    由于 souvlaki 在对战中的操作理论上都可以提前通过重排完成
    因此我们可以认为，对 souvlaki 最有利的重排就是直接对 a 排序

    所以最终是否胜利，取决于是否存在 a[odd] 和 a[odd + 1]，使得
    a[odd] != a[odd + 1]。只要存在这样的相邻数对，只需交换他们
    kalamaki 就可以获得胜利
    """
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n - 1, 2):
        p, q = a[i], a[i + 1]
        if p < q:
            print("no")
            return
    print("yes")


t = int(input())
for _ in range(t):
    run()
