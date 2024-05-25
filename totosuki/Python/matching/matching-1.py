from collections import deque, defaultdict

input_csv_path = "./src/input_p1_c3.csv"
output_csv_path = "./src/output_p1_c3.csv"

with open(input_csv_path) as f:
  data = f.read().rstrip().split("\n")
  data = [list(map(int, d.split(","))) for d in data]

N = len(data)
q = deque(list(range(N)))
d = defaultdict(lambda: -1)
priority = [0] * N

while len(q):
  next = []
  for _ in range(len(q)):
    id = q.popleft()
    num = data[id][priority[id]]
    if d[num] == -1:
      d[num] = id
    else:
      if priority[d[num]] < priority[id]:
        next.append(d[num])
        priority[d[num]] += 1
        d[num] = id
      else:
        next.append(id)
        priority[id] += 1
  q = deque(next)

ans = [0] * N
for i in range(N):
  ans[d[i]] = i

ans = ",".join(map(str, ans))

with open(output_csv_path, mode='w') as f:
  f.write(ans)