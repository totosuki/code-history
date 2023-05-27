N, M, H, K = map(int, input().split())
S = input()

def create_move_list(code: str):
    facing_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

    return [facing_dict[c] for c in list(code)]


def main():
    hp = H
    pos = [0, 0]
    move_list = create_move_list(S)
    item_list = [list(map(int, input().split())) for _ in range(M)]

    for m in move_list:
        hp -= 1

        pos = [pos[0] + m[0], pos[1] + m[1]]
        
        if pos in item_list and hp < K:

            hp = K
            item_list.remove(pos)

        if hp < 0:
            print("No")
            return
        
    print("Yes")

main()