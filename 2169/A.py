from bisect import bisect_left, bisect_right

t = int(input())
for _ in range(t):
    n, a = list(map(int, input().split()))
    balls = list(map(int, input().split()))
    left = bisect_left(balls, a)
    right = bisect_right(balls, a)
    # 左侧数字个数 = left
    # 右侧数字个数 = n - right
    if left > n - right:
        print(a - 1)
    else:
        print(a + 1)
