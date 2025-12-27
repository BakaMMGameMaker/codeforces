t = int(input())
LIMIT = 10**10
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))  # 所有 ai 两两不同
    # 数组内所有比 k 小的数字将永远是自己
    # 又因为 a 两两不同，如果 k 比 a 中最小的两个以上的数字大
    # 那么这些比 k 小的数字将永远不会发生变化，这样就不可能实现数组中所有数字相同
    # 如果 k = 第一小的数字，那么必然合法，如果 k > 第一小的数字，
    # 那么 k 需要满足 k 的上界 = 第二小的数字 - 第一小的数字
    # 因为当 k > min(a) 的时候，min(a) 不可能变化，要让第二小的数字
    # 变成 min(a)，k 就不应该超过第二小的数字 - 第一小的数字
    # 只要可以取到这一个值，对于更大的数字自然也能通过取 x = current - min(a)
    # 来实现 mod 到 min(a)
    fm = sm = LIMIT
    for num in a:
        if num < fm:
            sm = fm
            fm = num
        elif num < sm:
            sm = num
    print(max(fm, sm - fm))
