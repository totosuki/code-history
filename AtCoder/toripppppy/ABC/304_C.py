import math

N, D = map(int, input().split())

virus_list = []

for _ in range(N):
    virus_list.append(list(map(int, input().split())))


def get_euclid(a: list, b: list) -> int:
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


for i in range(5):
    for _ in range(N-1):
        x, y = map(int, input().split())

        virus_flag = False

        for v in virus_list:
            print([x, y], v, get_euclid([x, y], v))

            if get_euclid([x, y], v) <= D:
                virus_list.append([x, y])
                virus_flag = True
                break
                    
        print("Yes" if virus_flag else "No")