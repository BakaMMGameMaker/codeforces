def run():
    """
    由于全过程中的 x 位数不可能比 a 的位数更多，因为这意味着 x > a
    所以如果 b 的位数比 a 的位数多，可以提前判死刑

    如果 b 的位数比 a 的位数少，尝试直接构造
    11 1101 1100
    00 1111 0100
    首先构造 x1 让二者低位一致
    由于此处需要保留 a 的高位，所以 x1 的高位必定为 0，这也确保了 x1 <= a
    共同位只需要一样的地方为 0，不一样的地方为 1 即可
    => x1: 00 0010 1000
    =>  a: 11 1111 0100
    然后只需要去除高位即可，高位为 1，剩余位全为 0
    => x2: 11 0000 0000
    一定能在两次内搞定

    如果 b 的位数和 a 的位数一样，则只需要进行第一步
    由于 a 和 b 的最高位都是 1，因此 x1 的最高位一定为 0，不会比 a 大
    """
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
        return
    bina = bin(a)[2:]
    binb = bin(b)[2:]
    la = len(bina)
    lb = len(binb)
    if lb > la:
        print(-1)
        return
    df = la - lb
    bin2 = "0" + bina[:df] + "0" * lb  # 塞个最高位防止 runtime error
    x2 = int(bin2, base=2)
    bina = bina[df:]
    bin1 = "0"
    for i in range(lb):
        bin1 += "0" if bina[i] == binb[i] else "1"
    x1 = int(bin1, base=2)
    if df == 0:
        print(1)
        print(x1)
        return
    print(2)
    print(x1, x2)


t = int(input())
for _ in range(t):
    run()
