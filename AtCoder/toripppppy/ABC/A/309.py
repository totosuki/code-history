A, B = list(map(int, input().split()))

# def f(A, B):
#     if ((A-1)%3 == (B-1)%3 and abs((B-1)//3 - (A-1)//3) == 1) or ((A-1)//3 == (B-1)//3 and abs((B-1)%3 - (A-1)%3) == 1):
#         print("Yes")
#     else:
#         print("No")

# f(A, B)

r = list()

if A == 1:
    r = [2,4]
elif A == 2:
    r = [3,5]
elif A == 3:
    r = [6]
elif A == 4:
    r = [5,7]
elif A == 5:
    r = [6,8]
elif A == 6:
    r = [9]
elif A == 7:
    r = [8]
elif A == 9:
    r = []

print("YNeos"[B not in r::2])



A, B = list(map(int, input().split()))
[print("YNeos"[not (l[1]-l[0]==1 and(l[1]-1)//3==(l[0]-1)//3)::2])for l in[list(map(int,input().split()))]]
