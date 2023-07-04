S = input()
T = input()

def main():
    for s,t in zip(S,T):
        if s == t: continue

        if "@" in [s,t]:
            a = "".join([s,t]).replace("@","")

            if a in "atcoder": continue

        print("You will lose")
        return

    print("You can win")

main()

