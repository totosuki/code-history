N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    if i == 0:
        print(A[1][0],*A[0][:-1],sep="")
    elif i == N-1:
        print(A[-1][1:],A[i-1][-1],sep="")
    else:
        print(A[i+1][0],*A[i][1:-1],A[i-1][-1],sep="")