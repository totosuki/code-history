N, M = map(int,input().split())
# くった
C = input().split()
# 色
D = input().split()
# 値段
P = list(map(int,input().split()))
 
a = 0
 
for c in C:
    try:
        i = D.index(c) + 1
    except:
        i = 0

    a += P[i]
    
print(a)