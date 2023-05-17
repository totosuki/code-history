import os
import datetime

ディレクトリ = os.listdir('パス')
for i in ディレクトリ:
    パス = f'パス{i}'
    
    # システム時刻的なやつ
    経過時間 = os.stat(パス).st_birthtime
    # 日付に変換
    作成日時 = datetime.datetime.fromtimestamp(経過時間).strftime('%Y-%m-%d')
    os.rename(パス,f'パス{作成日時}{i}')

print(ディレクトリ)