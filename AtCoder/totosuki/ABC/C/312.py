import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
R = [0] * N
rslt = 0

for i in range(N):
  if i == 0:
    if B[0] < A[0]:
      R[i] = 1
    else:
      R[i] = 0
  else:
    R[i] = R[i-1]
  
  while R[i] < M and B[R[i]] < A[i]:
    R[i] += 1

print(R)

for i in range(N):
  if i+1 >= M - R[i] and M - R[i] != 0:
    if R[i] <= i:
      print(B[R[i]-1])
    else:
      print(A[i])
    break
else:
  if R[0] != 0:
    print(B[-1] + 1)
  else:
    print(B[M - N - 1] + 1)


# case
# 3 4
# 500 500 500
# 100 100 100 100