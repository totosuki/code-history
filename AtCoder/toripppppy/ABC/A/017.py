# [print(int(sum(list(map(lambda x:x[0]*x[1]*0.1,l)))))for l in[[list(map(int, input().split())) for _ in range(3)]]]

print(sum([eval(f"{l[0]}*{l[1]}//10")for l in[input().split()for _ in range(3)]]))