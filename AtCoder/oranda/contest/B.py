# A,B = input().split()
# S = len(A) if len(A) > len(B) else len(B)
# A,B = int(A),int(B)
# if 10**S <= A+B:
#     print("Hard")
# else:
#     print("Easy")

A,B = input().split()
for i in reversed(range(len(A) if len(A) > len(B) else len(B))):
    A[i] + B[i] <= 10
    