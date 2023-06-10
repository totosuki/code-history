def delete_char(S, T):
  for i, s in enumerate(S):
    if s == T[0]:
      S = S[:i] + S[i+1:]
      T = T[1:]
      return S, T
  print("NO")
  exit()

s = input()
t = input()
if s == t:
  print("NO")
  exit()

while True:
  if len(s) <= 0:
    print("YES")
    exit()
  s, t = delete_char(s, t)