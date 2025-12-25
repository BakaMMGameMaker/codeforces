from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    r = 0
    for num, count in c.items():
        if count > num:
            r += count - num
        if count < num:
            r += count
    print(r)
