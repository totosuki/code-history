N, K = map(int, input().split())
H = list(map(int, input().split()))

def dynamic_programming(H, N, K):
  #Preprocessing
  start_list = []
  if K > N:
    K = N
  for i in range(K):
    tmp = []
    if i == 0:
      tmp.append(0)
    else:
      for j in range(i):
        tmp.append(abs(H[i] - H[j]))
    start_list.append(min(tmp))

  l = start_list + [0] * (N-K)
  
  #DP
  for i in range(K, N):
    tmp = []
    for j in range(1, K+1):
      diff = l[i-j] + abs(H[i] - H[i-j])
      tmp.append(diff)
    l[i] = min(tmp)
  
  return l

l = dynamic_programming(H, N, K)
print(l[N-1])