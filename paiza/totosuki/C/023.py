hit_nums = list(map(int, input().split()))
N = int(input())
card_nums = [list(map(int, input().split())) for _ in range(N)]
rslt = []
for card_num in card_nums:
  count = 0
  for num in card_num:
    if num in hit_nums:
      count += 1
    else:
      continue
  rslt.append(count)
[print(r) for r in rslt]