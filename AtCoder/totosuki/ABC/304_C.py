import math
N, D = map(int, input().split())
pos_li = []
del_li = []
infection = []
count = 0

for _ in range(N):
  pos_li.append(list(map(int, input().split())))

infection.append(pos_li[0])

while True:
  for i, pos in enumerate(pos_li):
    for inf_pos in infection:
      dis = math.sqrt((inf_pos[0] - pos_li[i][0])**2 + (inf_pos[1] - pos_li[i][1])**2)
      if D - dis >= 0:
        infection.append(pos_li[i])
        count += 1
        break
    if D - dis < 0:
      pass
  if count >= N:
    break

for pos in pos_li:
  for inf_pos in infection:
    if pos == inf_pos:
      print("Yes")
      break
  if pos != inf_pos:
    print("No")


# for i, pos in enumerate(pos_li):
#   for inf_pos in infection:
#     dis = math.sqrt((inf_pos[0] - pos_li[i][0])**2 + (inf_pos[1] - pos_li[i][1])**2)
#     if D - dis >= 0:
#       infection.append(pos_li[i])
#       break
#   if D - dis < 0:
#     pass


# for i, pos in enumerate(pos_li):
#   for pos_2 in pos_li:
#     if pos == pos_2:
#       continue
    
#     dis = math.sqrt((pos[0] - pos_2[0])**2 + (pos[1] - pos_2[1])**2)
#     if D - dis >= 0:
#       print(f"pos: {pos}, pos_2: {pos_2}, dis: {dis}")
#       print("Yes")
#       break
#   if D - dis < 0:
#     print("No")
#     del_li.append(pos_li.index(pos_li[i]))