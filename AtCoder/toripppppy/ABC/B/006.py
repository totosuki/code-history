n = int(input())

l = [0,0,1]

if n <= 3:
  print(l[n-1])
  exit()

for i in range(3,n):
  l.append(sum(l[i-3:])%10007)
  
print(l[-1]%10007)
