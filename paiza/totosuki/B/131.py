N, M = map(int, input().split())
A = []
for _ in range(N):
  A.append(list(map(int, input().split())))
X = int(input())
R = []
for _ in range(X):
  R.append(list(map(int, input().split())))

#main
#新しいposの料金 - 過去に居た場所の料金がかかる金額
pos = [1, 1]
new_pos = [1, 1]
before_money = 0
rslt = 0

for i in range(X):
  pos = new_pos
  new_pos = R[i]
  before_money = A[new_pos[0] - 1][pos[1] - 1]
  after_money = A[new_pos[0] - 1][new_pos[1] - 1]
  rslt += abs(after_money - before_money)
  pos = R[i]

print(rslt)