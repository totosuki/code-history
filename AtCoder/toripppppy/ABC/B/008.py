l = [input() for _ in range(int(input()))]
print(sorted([(s,l.count(s)) for s in set(l)],key=lambda x:x[1])[-1][0])