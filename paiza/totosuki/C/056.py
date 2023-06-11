N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
pass_students = []
for i in range(len(data)):
  score = data[i][0] - (data[i][1] * 5)
  if score < 0:
    score = 0
  if score >= M:
    pass_students.append(i+1)
[print(i) for i in pass_students]