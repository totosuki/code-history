ATK, DEF, AGI = map(int, input().split())
N = int(input())
data = [list(input().split()) for _ in range(N)]
flag = False
for i in range(len(data)):
  check_count = 0
  if int(data[i][1]) <= ATK <= int(data[i][2]):
    check_count += 1
  if int(data[i][3]) <= DEF <= int(data[i][4]):
    check_count += 1
  if int(data[i][5]) <= AGI <= int(data[i][6]):
    check_count += 1
  if check_count == 3:
    flag = True
    print(data[i][0])

if not flag:
  print("no evolution")