N = int(input())
A = list(map(int, input().split()))
T, Q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(Q)]
for i in range(len(data)):
  pay = A[data[i][0]-1] * data[i][1]
  if pay > T:
    continue
  else:
    T -= pay
print(T)