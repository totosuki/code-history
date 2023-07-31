import random #ramdomモジュールをインポート
import time #timeモジュールをインポート

trials = 10000000 #試行回数
result = [0,0,0,0,0,0,0,0,0,0,0] #2から12までの配列
timeformat = '%Y/%m/%d %H:%M:%S' #YYYY/MM/DD 24時間表記hh:mm:ss

start = time.time() #開始時刻

for num in range(trials): #決めた試行回数分繰り返す
    x = random.randint(1,6) #ダイス1個目
    y = random.randint(1,6) #ダイス2個目
    z = x + y #二つのダイスの和
    if num % 1000000 == 0: #もし百万の倍数なら
        n = num // 1000000 #n百万を求める
        print ('なう' + str(n) + '百万') #n百万をお知らせする
    result[z-2] = result[z-2] + 1 #2から12を表す配列なので、2を引くことで2から配列を埋める
print(result) #結果をプリント

end = time.time() #終了時刻
time_diff = end - start #終了時刻から開始時刻を引いて、処理にかかった時間を求める

starttime = time.localtime(start) #UNIX時間をローカル時間に変換
endtime = time.localtime(end) #UNIX時間をローカル時間に変換

starttimeymdhms = time.strftime(timeformat , starttime) #struct_time形式になっている時間を変換
endtimeymdhms = time.strftime(timeformat , endtime) #struct_time形式になっている時間を変換

print('開始時刻' + str(starttimeymdhms) + ',' + '終了時刻' + str(endtimeymdhms) + ',' + '処理時間' + str(time_diff)) #開始時刻、終了時刻、処理時間をそれぞれプリント