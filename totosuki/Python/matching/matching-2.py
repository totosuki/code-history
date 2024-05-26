from collections import defaultdict, deque

input_csv_path = "./src/input_p1_c3.csv"
output_csv_path = "./src/output_p1_c3.csv"

def get_data():
  with open(input_csv_path) as f:
    data = f.read().rstrip().split("\n")
    data = [list(map(int, d.split(","))) for d in data]
  return data

def dfs(g, v, seen, route):
  seen[v] = True
  route.append(v)
  next = g[v]
  if seen[next]:
    return route, next
  else:
    return dfs(g, next, seen, route)

def reconstruct(N, g, can, data, priority):
  for i in range(N):
    if g[i] in can: continue
    while (data[i][priority[i]] not in can) and (priority[i] < N - 1):
      priority[i] += 1
    g[i] = data[i][priority[i]]
  return g

def solve(data):
  N = len(data)
  ans = [-1] * N
  can = set(range(N))
  priority = [0] * N
  
  g = defaultdict(int)
  for i in range(N):
    g[i] = data[i][0]
  
  while len(can):
    seen = [False] * N
    first_v = next(iter(can))
    route, close_v = dfs(g, first_v, seen, deque())
    
    while route[0] != close_v:
      route.popleft()
    
    for r in route:
      ans[r] = g[r]
    
    can -= set(route)
    
    g = reconstruct(N, g, can, data, priority)
  
  return ans

def write_data(ans):
  ans = ",".join(map(str, ans))
  with open(output_csv_path, mode='w') as f:
    f.write(ans)

def main():
  data = get_data()
  ans = solve(data)
  write_data(ans)

main()