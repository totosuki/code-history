[print(*list([n//2 + bool(n%2)] + list("2"*(n//2) + ("1" if n%2 != 0 else ""))), sep="\n") for n in [int(input())]]