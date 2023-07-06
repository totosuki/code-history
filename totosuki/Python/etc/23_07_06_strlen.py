# AtCoder Byte数(文字数)確認用

print("exitと入力で終了", end = "\n\n")

while True:
  text = input()

  if text == "exit":
    exit()
  
  print("{}byte".format(len(text)), end = "\n\n")