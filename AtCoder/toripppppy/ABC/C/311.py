import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
A = list(map(int, input().split()))

l = list()
s = set()

def search(point):
    next_point = A[point-1]

    if point in s:
        i = l.index(point)
        r = l[i:]
        # Output
        print(len(r))
        print(*r)

    else:
        l.append(point)
        s.add(point)
        search(next_point)


search(A[0])

