N, K = map(int, input().split())

l = []
d = 1

for _ in range(N):
    l.append(list(map(int, input().split())))


al = sorted(map(lambda x:x[0],l))
l = list(map(lambda x:x, l))

    
    