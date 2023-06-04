def fib(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print("フィボナッチ数列出力プログラムへようこそ！")
print("テストしたい方式の番号を入力して下さい")
print("個別に指定方式 (例: 4 6 2 210) ..... 1")
print("range()方式 (例: 1,10,2)............ 2")
index = int(input())
if index == 1:
  print("結果を見たい試行回数をスペース区切りで入力して下さい")
  test_nums = list(map(int, input().split()))
  for test_num in test_nums:
    print(f"試行回数{test_num}回 : {fib(test_num)}")
elif index == 2:
  print("結果を見たい範囲をスペース区切りで入力して下さい")
  start, end = map(int, input().split())
  for test_num in range(start, end + 1):
    print(f"試行回数{test_num}回 : {fib(test_num)}")
else:
  print("1か2を入力して下さい")