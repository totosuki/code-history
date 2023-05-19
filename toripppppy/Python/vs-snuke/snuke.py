### すぬけプライムと戦ってます
# https://atcoder.jp/contests/abc188/tasks/abc188_d

from inputter import inp

# 利用個数, すぬけプライムの定価
N, C = map(int, inp().split(" "))

# 注文のリスト
order_list = []

for _ in range(N):
    order_list.append(list(map(int, inp().split(" "))))

# イベント
event_list = []
# 今日
today = 1

for o in order_list:
    # 開始日なら
    if o[1] >= today:
        print(f"今日は{today}日。いっこかにゅうするよ")
        today = o[1]
    if o[2] >= today:
        print(f"今日は{today}日。いっこぬけるよ")