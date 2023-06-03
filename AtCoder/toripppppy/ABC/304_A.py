N = int(input())

s_list = []

nensho = ""
a = 10**9

for _ in range(N):
    s = input().split()

    if int(s[1]) < a:
        a = int(s[1])
        nensho = s[0]

    s_list.append(s[0])


i = s_list.index(nensho)

r = s_list[i:] + s_list[:i]

print(*r, sep="\n")

