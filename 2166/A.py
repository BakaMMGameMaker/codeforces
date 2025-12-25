t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    # 最后一个字符没办法被改变
    # 所有字符串只能变成 n * last char
    # 所以答案就是不等于 last char 的个数
    print(sum(1 if s[i] != s[-1] else 0 for i in range(n - 1)))
