A, B = map(int, input().split())
result = A / B
print(int(result))
amari = A % B
print(amari)
if amari <= 0:
  print(int(result))
else:
  print(int(result) + 1)