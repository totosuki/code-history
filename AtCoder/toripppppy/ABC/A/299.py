# print("in" if S.replace(".", "")[1] == "*" else "out")

[print("in" if input().replace(".", "")[1] == "*" else "out") if i == 1 else input() for i in range(2)]