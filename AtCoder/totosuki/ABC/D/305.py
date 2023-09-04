import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

def binary_search(x):
  left = -1
  right = N
  
  while right - left > 1:
    mid = (left + right) // 2
    if A[mid] <= x:
      left = mid
    else:
      right = mid

  return left

# 累積和
S = [0] * N
for i in range(1, N):
  S[i] = S[i-1]
  if i % 2 == 0:
    S[i] += A[i] - A[i-1]

for _ in range(Q):
  left, right = -1, N
  l, r = map(int, input().split())
  
  start = binary_search(l)
  end = binary_search(r)
  
  if start % 2:
    start_sm = S[start] + (l - A[start])
  else:
    start_sm = S[start]
  
  if end % 2:
    end_sm = S[end] + (r - A[end])
  else:
    end_sm = S[end]
  
  print(end_sm - start_sm)