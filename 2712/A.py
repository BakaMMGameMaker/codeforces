scores = list(map(lambda x: int(x), input().split()))
scores.sort()
mx = scores[-1]
mn = scores[0]
if mx - mn >= 10:
    print("check again")
else:
    print(f"final {scores[1]}")
