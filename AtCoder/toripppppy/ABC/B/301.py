N = int(input())
A_list =list(map(int, input().split()))

r = []

for i in range(N-1):
    l = A_list[i:i+2]
    print(l)
    r.append(l[0])
    r.append()

print(r)