T = int(input())

al = "abcdefghijklmnopqrstuvwxyz"

def judge(_: int, s: str):
    # 順序を整えないset()
    l = []
    for c in s:
        if c not in l:
            l.append(c)

    # alの部分文字列かどうか
    print("YNeos"["".join(l) not in al::2])


for _ in range(T):
    N = int(input())
    S = input()
    judge(N, S)