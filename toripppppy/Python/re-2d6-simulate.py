import random #ramdomモジュールをインポート
import time #timeモジュールをインポート


TRIALS = 10000000 #試行回数
TIME_FORMAT = '%Y/%m/%d %H:%M:%S' #YYYY/MM/DD 24時間表記hh:mm:ss

result = dict(zip(range(2, 13), [0]*11)) #2から12までのdict


def get_2d6():
    # 2d6の結果を返す
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return d1 + d2


def unix_to_str(unix_time: float):
    # UNIX時間から文字列にフォーマット
    struct_time = time.localtime(unix_time)
    ymdhms = time.strftime(TIME_FORMAT , struct_time)
    return ymdhms


### 計測開始
start = time.time()

for i in range(TRIALS): # 決めた試行回数分繰り返す
    d_sum = get_2d6() # 2d6を取得する
    result[d_sum] += 1 # 取得結果に応じて集計

    if i % 1000000 == 0: #もし百万の倍数なら
        n = i // 1000000 #n百万を求める
        print (f'なう{n}百万') #n百万をお知らせする

print(f'試行結果: {result}') #結果を出力

### 計測終了
end = time.time()


# 計測開始・終了時間を文字列にフォーマット
start_ymdhms = unix_to_str(start)
end_ymdhms = unix_to_str(end)

# 終了時刻から開始時刻を引いて、処理にかかった時間を求める
time_diff = end - start

# 開始時刻、終了時刻、処理時間をそれぞれ出力
print(f'開始時刻: {start_ymdhms}\n終了時刻: {end_ymdhms}\n処理時間: {time_diff}')