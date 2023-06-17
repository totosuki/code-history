import random
import time

#help機能を後で作りたいです。

#プレイヤーネームを文章に入れたい時とかに使う
#使い方 in_text(入れたい文章,入れたい言葉)
#変数名 = '私の名前は{}です'
#上のように入れたいテキストの部分に{}を置くこれだけ
def in_text(text,player_name):
    print(text.format(player_name))

#プログラム開始時に実行、次のプログラムまで2秒のスリープ
print('ようこそ冒険者様、貴方をお待ちしておりました')
time.sleep(2)

#実行後、次のプログラムまで1.5秒スリープ
print('格好を見るに未経験者様ですね？')
time.sleep(1)
print('わかりました')
time.sleep(1.5)

#入力受付開始(justiceロック解除)
print('では、お名前をお書きください')
justice = True

#入力可能かどうか？現在のプログラムだと受け取っちゃうので後で変更が必要

#入力された文字を受け取り表示
player_name = input()
aiu ='{}さんですね、次に希望役職をお選びください'
in_text(aiu,player_name)

#0.5秒スリープ
time.sleep(0.5)

#指定の役職以外を受け取った時にループする用変数
repeat = True
while repeat:
    #役職一覧みたいになる
    for i in job_title:
        print(i[0] +'を希望なら'+i[0]+'と')
    print('入力してください')

    #入力を受け取取る
    job_name = input()
    if(job_name):
        #次のif文をjobの数だけ行う
        for i in job_title:
            #受け取った入力と同じ文字があるか?あるならそれのindexをとる
            if( i[0] == job_name):
                print(i[0]+'ですね？')
                #受け取ったjobとプレイヤーネームを持ったPlayerを作成
                player = Player(player_name,job_title.index(i))
                print('ではこれで登録完了です')
                print('それではよき冒険ライフを！')
                #役職が決まり、playerを生成できた為ループ終了
                repeat = False

