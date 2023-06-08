N, M = map(int, input().split())

mohan = [int(input()) for _ in range(M)]
p_list = []

for _ in range(N):
    p = 100
    for m in range(M):
        d = abs(int(input()) - m)

        if d <= 10:
            p -= 1
        elif d <= 20:
            p -= 2
        elif d <= 30:
            p -= 3
        else:
            p -= 5

    print(p)

