N, c_1, c_2 = map(int, input().split())
P = [int(input()) for _ in range(N)]
kabu = 0
rslt = 0
for i, p in enumerate(P):
  if i == N - 1:
    rslt += p * kabu
    break

  if p <= c_1:
    kabu += 1
    rslt -= p
  elif p >= c_2:
    rslt += p * kabu
    kabu = 0
print(rslt)