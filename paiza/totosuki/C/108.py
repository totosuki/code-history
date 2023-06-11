N = int(input())
X = [int(input()) for _ in range(N)]
C = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
Y = [int(input()) for _ in range(K)]

time = X[Y[0]-1]
for i in range(1, K):
  time += C[Y[i-1]-1][Y[i]-1] + X[Y[i]-1]
print(time)