import itertools

N, M = map(int, input().split())

pairs_list = []

for _ in range(M):
    members = list(map(int, input().split()))
    
    pairs = []

    for i in range(0, N-1):
        pairs.append(tuple(sorted([members[i], members[i+1]])))

    for p in pairs:
        pairs_list.append(p)

patterns = list(itertools.combinations(range(1, N + 1), 2))
pairs_list = list(set(pairs_list))

result = [i for i in patterns if i not in pairs_list]

print(len(result))