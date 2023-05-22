import re
 
# テストケースの数
T = int(input())
 
def f(_, s):
    # _: 文字数, s: 文字列
    s2 = s[:-1]
    a_list = [m.start() for m in re.finditer('A', s2)]
    b_list = [i for i in range(len(s2)) if i not in a_list]
 
    s3 = s[1:]
 
    result = ""
 
    for i in a_list + b_list:
        result += s3[i]
 
    return result
 
 
for _ in range(T):
    N = int(input())
    S = input()
 
    while len(S) > 1:
        S = f(N, S)
 
    print(S)