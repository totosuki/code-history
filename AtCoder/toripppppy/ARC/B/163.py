

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = list(map(lambda x: x - A[0], A))[1:]

print(A, sorted(A[1:]))

print(sorted(A[1:], key=lambda x: abs(x - A[0])))

k = A[0]

l1 = [a for a in A[1:] if k <= a]
l2 = [a for a in A[1:] if k > a]
print(sum(l1)//len(l1), sum(l2)//len(l2))