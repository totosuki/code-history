import sys
input = sys.stdin.buffer.readline

K = int(input())
A, B = map(lambda x: int(x, K), input().split())

print(A * B)