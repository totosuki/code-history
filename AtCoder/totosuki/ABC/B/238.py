import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
angle = 0
L = [False] * 360
L[0] = True
rslt = list()

for a in A:
  angle += a
  angle %= 360
  L[angle] = True

cnt = 0
for i in range(360):
  cnt += 1
  if L[i] == True:
    rslt.append(cnt)
    cnt = 0
else:
  cnt += 1
  rslt.append(cnt)

print(max(rslt))