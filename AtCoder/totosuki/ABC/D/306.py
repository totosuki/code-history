import itertools

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
# conditions = [data[i][0] for i in range(len(data))]
# group = [(k,list(i)) for k, i in itertools.groupby(conditions)]
# group = [list(data) for data in group]
# print(group)
scores = []
i = 0
flag = False

while i < N:
  if data[i][0] == 0 and data[i][0] >= 0:
    scores.append(data[i][1])
  elif data[i][0] == 1:
    tmp = []
    while data[i][0] == 1:
      tmp.append(data[i][1])
      i += 1
      if i >= N:
        flag = True
        break
    tmp2 = []
    if not flag:
      while data[i][0] == 0:
        tmp2.append(data[i][1])
        i += 1
        if i >= N:
          flag = True
          break
    maxtmp = max(tmp)
    if tmp2:
      maxtmp = maxtmp + max(tmp2)
    scores.append(maxtmp)

  i += 1
print(scores)


# i = 0
# j = 0
# for _ in range(2):
#   #初期設定
#   scores = [0] * N
#   tmp = []

#   for _ in range(len(*group[i][1:])):
#     tmp.append(data[j][1])
#     j += 1
  
#   print(*group[i+1][1:])
#   j += len(group[i+1][1:])
#   i += 2

#   print(tmp)





# scores = [0] * N
# condition = 0

# for i in range(N):
#   if i == 0:
#     if 0 > 
#     scores[i] = max([0, data[0][1]])
#   else:
#     scores[i] = max([scores[i-1], scores[i-1]+data[i][1]])

# print(scores)
