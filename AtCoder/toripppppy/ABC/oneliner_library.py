### onelinerの定石

# 入力が一列、単体
[print(s) for s in [input()]]

# 入力が一列、複数（かつint）
[print(l) for l in [list(map(int, input().split()))]]

# 入力が複数行複数行、特定の入力のみを受け取る
[print(input()) if i == 1 else input() for i in range(2)]