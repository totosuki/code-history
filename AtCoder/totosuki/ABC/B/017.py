# [print(x) for S in [["ch","o","k","u"]] for t in [input()] for x in list(list(map(lambda s:t.replace(s,""),S)))]

x = input()
for c in ["ch","o","k","u"]:
  x = x.replace(c, "")
print("YES") if not x else print("NO")

# if not X: print("YNEOS"[bool(x)::2]) 
#   print("YES")
# elif X[-1] in "oku":
#   print("YES")
# elif X[-2:] == "ch":
#   print("YES")
# else:
#   print("NO")