# 記録の数
N = int(input())

# 奇数:起床, 偶数:就寝
log = list(map(int, input().split()))

def get_index(t):
  l = sorted(log + [t+1])
  return l.index(t+1)


def is_awake(t):
  return get_index(t) % 2 != 0


def get_range(ql:list):
  start = get_index(ql[0])
  end = get_index(ql[1])
  return log[start:end]

Q = int(input())

for _ in range(Q):
  ql = list(map(int,input().split()))
  
  l = get_range(ql)
  print(l)
  
  it = iter(l)
  awake_l = [j-i for i, j in zip(it, it)]
  it = iter(l[1:]+[l[0]])
  sleep_l = [j-i for i, j in zip(it, it)]
  
  add = 0
  try:
    if is_awake(ql[1]):
      add = ql[1]- l[-1]
    else:
      add = ql[1]- l[-1]
  except:
    pass
 
  
  sum_time = ql[1]-ql[0]
  print(sum_time)
  print(s)
  
  if is_awake(ql[0]):
    print(sum_time-sum(s) + add)
  else:
    print(sum_time-sum(a) + add)