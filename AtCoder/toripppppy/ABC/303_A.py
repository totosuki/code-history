# N = int(input())
# S = input()
# T = input()

# def is_similar(x: str, y: str):
#     return (x, y) == ("1", "l") or (x, y) == ("0", "o") or (y, x) == ("1", "l") or (y, x) == ("0", "o") or x == y

# def judge():
#     for s, t in zip(S, T):
#         if not is_similar(s, t):
#             print("No")
#             return

#     print("Yes")

# judge()


[print("Yes" if all((s, t) in l[3] or (t, s) in l[3] or s == t for s, t in zip(l[1], l[2])) else "No") for l in [[input() for _ in range(3)] + [[("1","l"),("0","o")]]]]