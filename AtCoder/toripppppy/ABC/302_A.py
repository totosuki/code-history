# A, B = map(int, input().split())
# print(A // B + (A % B != 0))

[print(l[0] // l[1] + (l[0] % l[1] != 0)) for l in [list(map(int, input().split()))]]