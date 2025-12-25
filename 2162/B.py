t = int(input())
for _ in range(t):
    """
    显然，只要把所有 0 都删掉，剩下的子串肯定是回文串
    """
    n = int(input())
    s = input()
    a: list[int] = []
    for i in range(n):
        if s[i] == "0":
            a.append(i + 1)
    print(len(a))
    for i in a:
        print(i, end=" ")
    print()
