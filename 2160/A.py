t = int(input())
for _ in range(t):
    """
    考虑特殊情况，整个 a 作为一个子多重集合
    根据条件，最终 mex 只能是这个子多重集合的 mex
    """
    n = int(input())
    a = list(map(int, input().split()))
    omg = [False for _ in range(101)]
    for num in a:
        omg[num] = True
    for num, o in enumerate(omg):
        if not o:
            print(num)
            break
