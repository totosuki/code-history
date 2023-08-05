import sys, statistics
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
mid = int(statistics.mean(A))
rslt = 0

for i in A:
  rslt += abs(mid - a)

print(rslt // 2)

# dict = defaultdict(int)
# cnt = 0

# # dict設定
# for a in A:
#   dict[a] += 1

# keys = dict.keys()
# mx = max(keys)
# mn = min(keys)

# while True:
#   # max
#   if dict[mx] != 0:
#     dict[mx] -= 1
#     dict[mx-1] += 1
#   else:
#     mx -= 1
#     dict[mx] -= 1
#     dict[mx-1] += 1
#   # min
#   if dict[mn] != 0:
#     dict[mn] -= 1
#     dict[mn + 1] += 1
#   else:
#     mn += 1
#     dict[mn] -= 1
#     dict[mn + 1] += 1
#   if mx - mn <= 1:
#     break
#   else:
#     cnt += 1

# print(cnt)