S = input() + ";"
r = ""
c = 0
m = ""

for s in S:
    if m != s:
        r += m + str(c)
        m = s
        c = 0

    c += 1

print(r[1:])