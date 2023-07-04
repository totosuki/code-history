import sys
input = sys.stdin.buffer.readline

N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
rslt = int()

for a,b in zip(A, B):
  rslt += a*b

print("Yes") if rslt == 0 else print("No")