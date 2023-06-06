S = sorted(input())
N = int(input())

print(S[(N-1)//len(S)] + S[(N-1)%len(S)])