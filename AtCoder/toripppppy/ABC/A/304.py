# N = int(input())

# s_list = []

# nensho = ""
# a = 10**9

# for _ in range(N):
#     s = input().split()

#     if int(s[1]) < a:
#         a = int(s[1])
#         nensho = s[0]

#     s_list.append(s[0])


# i = s_list.index(nensho)

# r = s_list[i:] + s_list[:i]

# print(*r, sep="\n")

[[print(l2) for l2 in [[r[0] for r in l].index(sorted([r[1] for r in l])[0]) for l in [list(map(lambda x: [x[0], int(x[1])], [input().split() for _ in range(n)]))]]] for n in [int(input())]]