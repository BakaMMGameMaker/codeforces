t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    o = 0
    e = 0
    for num in a:
        if not o and num & 1:
            o = 1
        if not e and not num & 1:
            e = 1
        if o and e:
            break
    if o and e:
        a.sort()
    for num in a:
        print(num, end=" ")
    print()
