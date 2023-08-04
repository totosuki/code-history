N = int(input())

def f(n):
  n -= 10*(len(str(n))-1) - 1
  return n
  
r = 0
for i in range(1,N+1):
  r += f(i)
  
print(r)