# [print("YES" if "3" in s or int(s)%3 == 0 else "NO") for s in [input()]]

# [print('YNEOS'[not ("3"in s or int(s)%3==0)::2]) for s in [input()]]

[print('YNEOS'[(s%3) ^ ("3" in s)::2]) for s in [int(input())]]