product = []
N,M = map(int, input().split())
for i in range(N):
    product.append(list(map(int, input().split())))

ジャスティス = False

product.sort(reverse=True)
for i in product:
    for j in product[0:product.index(i)]:
        if i[1] <= j[1]:
            I = []
            J = []
            for _ in range(i[1]):
                I.append(i[2+_])
                J.append(j[2+_])
            if I == set(I) & set(J):
                ジャスティス = True

if ジャスティス:
    print("Yes")
else:
    print("No")




# product = []
# cost = []
# func = []

# N,M = map(int, input().split())
# for i in range(N):
#     product.append(list(map(int, input().split())))
#     cost.append(product[i][0])
#     func.append(product[i][1])
# high_rank = product.copy()
# low_rank = product.copy()




# for i in high_rank:
#     i[0]

# for i in range(len(product)):
#     print(f'=>{product[i]}:{cost[i]}:{func[i]}')


