T = int(input())

al = "abcdefghijklmnopqrstuvwxyz"

def judge(_: int, s: str):
    i = al.index(s[0])
    for c in s:
        if len(set(s)) == 1:
            print("Yes")
            return
        
        if i < al.index(c):
            i = al.index(c)

    if i != al.index(s[0]):
        print("Yes")
    else:
        print("No")


for _ in range(T):
    N = int(input())
    S = input()
    judge(N, S)