N,M = map(int,input().split())
S = []
cnt = 0

for i in range(N):
    S.append(input())

for i in range(N-9):
    for l in range(M-9):

        judge = True
        for k in range(4):
            for j in range(4):
                
                if k or j == 4:
                    if S[i+k][l+j] != '.':
                        print(i,l,"b",k,l)
                        judge = False
                else:
                    if S[i+k][l+j] != '#':
                        print(i,l,"a",k,l,S[i+k][l+j])
                        judge = False

        for k in range(4):
            for j in range(4):

                if k or j == 4:
                    if not S[(i+9)-k][(l+9)-j] != '.':
                        print(i,l,"d",k,l)
                        judge = False
                else:
                    if not S[(i+9)-k][(l+9)-j] != '#':
                        print(i,l,"c",k,l)
                        judge = False

        if judge:
            cnt = cnt + 1

print(cnt)