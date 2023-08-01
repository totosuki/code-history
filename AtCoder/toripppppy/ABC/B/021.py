N = int(input())
a, b = map(int, input().split())
K = int(input())
pl = map(int, input().split())

kl = list(range(1, N+1))

kl.remove(a)
kl.remove(b)

for p in pl:
    try:
        kl.remove(p)
    except:
        print("NO")
        exit()

print("YES")