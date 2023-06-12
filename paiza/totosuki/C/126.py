A, B, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
rslt = A*2
for i in range(1, len(data)):
  day_diff = data[i][0] - data[i-1][1]
  if day_diff == 1:
    rslt += B
  elif day_diff >= 2:
    if B*day_diff < A*2:
      rslt += B*day_diff
    else:
      rslt += A*2
print(rslt)