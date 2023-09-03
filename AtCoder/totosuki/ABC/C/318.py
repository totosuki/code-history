# 130byte
# i="map(int,input().split())"
# N,D,P=eval(i)
# F=list(eval(i))
# F.sort(reverse=1)
# print(sum(min(P,sum(F[i:i+D]))for i in range(0,N,D)))

# import sys
# input = sys.stdin.buffer.readline

# N, D, P = map(int, input().split())
# F = list(map(int, input().split()))
# F.sort(reverse = True)
# rslt = 0

# for i in range(0, N, D):
#   sm = sum(F[i:i + D])
#   if sm < P:
#     rslt += sm
#   else:
#     rslt += P

# print(rslt)