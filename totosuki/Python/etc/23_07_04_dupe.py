# AtCoderのファイル作成用

start_num = 1 # 増やしたいフォルダの最初の数
end_num = 100 # 増やしたいフォルダの最後の数

for num in range(start_num, end_num+1):
  file_name = str(num).zfill(3)
  try:
    f = open(f"{file_name}.py", mode = "x")
    f.close()
  except:
    print(f"{file_name}.pyは既に存在します")