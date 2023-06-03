# import itertools

# N = int(input())

# a_list = list(map(int, input().split()))

# max = 0


# for a in itertools.permutations(a_list, len(a_list)):
	
#     it = iter(a)
#     a = [i ^ j for i, j in zip(it, it)]


#     r = sorted(a)[int(len(a)/2)]

#     if r > max: max = r

# print(max)

print(0 ^ 5)