import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N = int(input())
d = defaultdict(list)
li = []
ice_dict = defaultdict(int)

for _ in range(N):
  F, S = map(int, input().split())
  
  # 異なる方
  if ice_dict[F]:
    if S > ice_dict[F]:
      ice_dict[F] = S
  else:
    ice_dict[F] = S

  # 同じ方
  if len(d[F]) < 2:
    d[F].append(S)
  else:
    if d[F][1] > d[F][0]:
      d[F][1], d[F][0] = d[F][0], d[F][1]
    if S > d[F][1]:
      d[F][1] = S

for key in d.keys():
  if len(d[key]) == 2:
    if d[key][1] > d[key][0]:
      d[key][1], d[key][0] = d[key][0], d[key][1]
    a, b = d[key]
    li.append(a+(b//2))

diff_list = sorted(ice_dict.values())
diff_rslt = 0
if len(diff_list) >= 2:
  diff_rslt = sum([diff_list[-1],diff_list[-2]])

same_rslt = max(li) if li else 0

print(max(same_rslt, diff_rslt))