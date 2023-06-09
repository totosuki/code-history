N = int(input())
S_1 = input()
S_2 = input()
for _ in range(N):
  if S_1 == S_2:
    print("Yes")
    exit()
  S_1 = S_1[1:] + S_1[0]
print("No")