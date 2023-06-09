xc, yc, r_1, r_2 = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
for xy in XY:
  if r_1**2 <= ((xy[0]-xc)**2 + (xy[1]-yc)**2) <= r_2**2:
    print("yes")
  else:
    print("no")