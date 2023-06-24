# p, q = sorted(map(list("ABCDEFG").index, input().split()))
# print(sum([3,1,4,1,5,9][p:q]))

# 未検証
for l in[list(sorted(map(list("ABCDEFG").index, input().split())))]:print(sum([3,1,4,1,5,9][l[0]:l[1]]))