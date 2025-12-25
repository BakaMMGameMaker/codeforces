q = int(input())
for _ in range(q):
    n = int(input())
    s, t = input().split()
    counter = [0 for __ in range(26)]
    a = ord("a")
    fail = 0
    for c in s:
        c = c.lower()
        idx = ord(c) - a
        counter[idx] += 1
    for c in t:
        c = c.lower()
        idx = ord(c) - a
        if counter[idx] == 0:
            fail = 1
            break
        else:
            counter[idx] -= 1
    if fail:
        print("NO")
    else:
        print("YES")
