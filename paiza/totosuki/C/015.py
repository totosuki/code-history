N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
point = 0
for d in data:
  rate = 0.01
  if "3" in str(d[0]):
    rate = 0.03
  elif "5" in str(d[0]):
    rate = 0.05
  point += int(d[1] * rate)
print(point)