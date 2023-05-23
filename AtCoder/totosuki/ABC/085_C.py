N, Y = map(int, input().split())

#N枚を10000, 5000, 1000の３つのループ
for n_10000 in range(N + 1):
  for n_5000 in range((N - n_10000) + 1):
    for n_1000 in range((N - n_10000 - n_5000) + 1):
      print(n_10000)
      print(n_5000)
      print(n_1000)
      break
    break
  break