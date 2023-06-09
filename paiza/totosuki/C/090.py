S = input().replace("-", "")
len_l = [12,3,4,5,6,7,8,9,10,11]
rslt = 0
for s in S:
  rslt += len_l[int(s)] * 2
print(rslt)