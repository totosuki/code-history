# print(*filter(lambda x: x % 2 == 0, l))

[print(*filter(lambda x: x % 2 == 0, map(int, input().split()))) if i == 1 else input() for i in range(2)]