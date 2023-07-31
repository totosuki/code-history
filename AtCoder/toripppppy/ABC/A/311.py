N = int(input())
S = input()

for i in range(1,N+1):
  s = S[:i]
  if "A" in s and "B" in s and "C" in s:
    print(i)
    break