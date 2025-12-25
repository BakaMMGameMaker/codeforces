t = int(input())
for _ in range(t):
    """
    According to the formula, it is not difficult to see that the
    final result of the expression inside the absolute value is simply
    the last number in the array minus the first number. Therefore,
    the problem reduces to making the lexicographical order as small as possible,
    and there are only four cases to consider:

    Case 1: Neither the first nor the last element is -1. Then the minimum result is
    the last element minus the first element, and the -1s in the middle are changed to 0.

    Case 2: One of the first or last element is -1. Then the minimum result is 0.
    We only need to change the -1 at the start or end to the value of the end or start element,
    respectively, and change the -1s in the middle to 0.

    Case 3: Both the first and last elements are -1. Then the minimum result is 0,
    and we only need to change all -1s to 0.
    """
    n = int(input())
    l = list(map(int, input().split()))
    b = l[0]
    e = l[n - 1]
    r = 0
    if b != -1 and e != -1:
        r = e - b
    elif b != -1 and e == -1:
        e = b
        r = 0
    elif b == -1 and e != -1:
        b = e
        r = 0
    else:
        b = e = 0
        r = 0
    print(abs(r))
    print(b, end=" ")
    for i in range(1, n - 1):
        num = l[i]
        if num == -1:
            print(0, end=" ")
        else:
            print(num, end=" ")
    print(e)
