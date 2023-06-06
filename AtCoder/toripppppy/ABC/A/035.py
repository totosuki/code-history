import math

W, H = map(int, input().split())

g = math.gcd(W, H)

print(f"{W//g}:{H//g}")