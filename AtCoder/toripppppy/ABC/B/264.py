[print("wbhliatcek"[(l[0]%2 if l[1]>l[0] else l[1]%2)::2])for l in[list(map(lambda x:abs(eval(f"{x}-({x}>8)*16")),input().split()))]]