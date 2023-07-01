import itertools

N = int(input())
l = [input() for _ in range(N)]
lc = list(itertools.combinations(l,2))

l = set()

for c in lc:
  c1 = "".join(c)
  c2 = "".join([c[1], c[0]])
  l.add(c1)
  l.add(c2)
  
  
for c in l:
  if c == "".join(list(reversed(list(c)))):
    print("Yes")
    exit()
    
print("No")