### inputter
# input.txtを標準入力として使用できる inp()関数 を実装（挙動はinput()と一緒）

INPUT_LIST = []

with open("AGC/input.txt") as f:
    # 一行ずつ読み込んで配列化
    INPUT_LIST = list(map(lambda s: s.rstrip(), f.readlines()))

def inp() -> str:
    # 一番初めの要素を削除して返す
    return INPUT_LIST.pop(0)