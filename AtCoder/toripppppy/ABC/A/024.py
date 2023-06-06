A, B, C, K = map(int, input().split())
S, T =  map(int, input().split())

fee = A*S + B*T - (C*(S+T) if S+T >= K else 0)

print(fee)