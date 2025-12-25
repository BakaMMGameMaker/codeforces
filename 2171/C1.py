t = int(input())
for _ in range(t):
    """
    # 1. If XA and XB are originally equal, then no matter
    # how many digits we swap, it will not affect the final tie.
    # 2. If XA and XB are not equal, then no matter how we swap
    # at the end, it is impossible to create a tie. First,
    # ignore all indices where the digits on both sides are equal,
    # because swapping them will not change the outcome. Next,
    # look at the last position where the digits on both sides are
    # different. If the optimal solution up to this point would lead
    # to a tie, then the person who controls the last '1' will win.
    # For example, 0,0 means keeping the '1' for oneself, and 1,1 means
    # giving the '1' to the opponent. If the optimal solution leads to
    # 0,1 or 1,0, then whoever controls the last '1' will result in a tie,
    # but this situation cannot occur. Therefore, whoever controls the
    # last '1' will achieve victory.
    """
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    xa = 0
    xb = 0
    ld = 0  # last difference
    for i in range(n):
        na = a[i]
        nb = b[i]
        xa ^= na
        xb ^= nb
        if na != nb:
            ld = i
    if xa == xb:
        print("Tie")
    else:
        if ld % 2 == 0:
            print("Ajisai")
        else:
            print("Mai")
