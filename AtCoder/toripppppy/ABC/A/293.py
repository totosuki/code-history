# swap odd and even

[print(*[s[x:x+2][::-1] for x in range(0, len(s), 2)], sep="") for s in [input()]]