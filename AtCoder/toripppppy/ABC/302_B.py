H, W = map(int, input().split())

print(H, W)

m = []

for _ in range(H):
    m.append(input())


n = len(m)
rl_map = ["".join([m[max(0, -d) + i][max(0, d) + i] for i in range(n - abs(d))]) for d in range(1-n, n)]
lr_map = ["".join([m[max(0, d) + i][min(n + d, n) - i - 1] for i in range(n - abs(d))]) for d in range(1 - n, n)]


pos = []

for j, s in enumerate(rl_map):
    if "snuke" in s:
        pos = [j]

for j, s in enumerate(lr_map):
    if "snuke" in s:
        i = j

print(i)
print(rl_map)


"""
6 6
sgxgpu
ankxks
zhubpp
hykkkk
esnuee
zplvfj
"""