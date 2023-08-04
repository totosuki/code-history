import math

N = int(input())


def f(n,k):
    t = int(math.log(n-(n%3), 3))

    n -= 3**t

    print(n,)

    if n >= 2:
        print("Yes")
    else:
        if k == 1:
            print("No")
            return
        
        f(n, k-1)


for _ in range(N):
    n, k = map(int, input().split())
    f(n,k)