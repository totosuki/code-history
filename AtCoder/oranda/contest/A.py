S = []
S.append(input())
S.append(input())

if (S[0][0] in '#' and S[1][1] in '#' ) and (S[0][1] in '.' and S[1][0] in '.'):
    print("No")
elif (S[0][0] in '.' and S[1][1] in '.' ) and (S[0][1] in '#' and S[1][0] in '#'):
    print("No")
else:
    print("Yes")