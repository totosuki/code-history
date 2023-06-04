#ユークリッドの互助法
#aとbの最大公約数を求める
def gcd(a, b):
  if a < b:
    return gcd(b, a)
  else:
    if a % b == 0:
      return b
    else:
      return gcd(b, a % b)