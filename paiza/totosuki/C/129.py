N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
B = [int(input()) for _ in range(M)]
A_nodupe = list(set(A))
A_count = list(map(A.count, A_nodupe))
B_count = list(map(B.count, A_nodupe))
if A_count == B_count:
  print("Yes")
else:
  print("No")