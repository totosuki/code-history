K, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(K)]
for i in range(len(data)):
  date = data[i][0]
  score = (100 // N) * data[i][1]
  if date > 0:
    if date <= 9:
      score = score * 0.8
    elif date >= 10:
      score = 0
  
  if score >= 80:
    print("A")
  elif score >= 70:
    print("B")
  elif score >= 60:
    print("C")
  else:
    print("D")
