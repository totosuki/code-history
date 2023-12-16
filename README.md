# code-history
## code-historyとは？
過去に書いたコードをアーカイブ的にまとめたリポジトリ。
## code-hitosryの使い方
世界一簡単です。<br>
Cloneしたローカルリポジトリに、アーカイブ化したいファイルを入れるだけ！！
## ディレクトリ構造について
`名前 -> 言語 -> 整理用のフォルダ(無くてもOK) -> アーカイブ化したいファイル`で基本まとめてます。<br><br>
以下はディレクトリ構造の例
- takahashi
  - Python
    - practice
      - test.py
      - todo.ipynb
      - winlos.py
    - inSchool
      - 1st.py
      - 2nd.py
      - 3rd.ipynb
    - etc
      - siran.py
      - nannka.py
  - Kotlin
  - COBOL
## 注意点
- <b>他の人のコードを見たいときは、元データに変更を加えないようにしてね！</b>(複製やコピーで🙏)
- `.gitignore`はいじらないでね！！
- 個人情報は乗らないように気をつけよう。(絶対パスやトークン、メールアドレスなど)
- パスが入ってるコードは`path/to/hoge.csv`などに変更するの推奨。
- `.ipynb`は可能な限り出力結果を消してからアーカイブ化して下さい。(出力結果によってはファイルサイズやばくなるよ)
## その他のフォルダ
### OctoMouse
マウスやキーボードの入力数などが分かるアプリ[OctoMouse](https://github.com/KonsomeJona/OctoMouse)のcsvデータ出力をまとめたフォルダ。
### AtCoder
競技プログラミングサイト[AtCoder](https://atcoder.jp/home)のコードをまとめたフォルダ。<br><br>
以下は推奨ディレクトリ構造
- AtCoder
  - takahashi
    - ABC
      - A
        - 004.py
        - 999.py
      - B
        - 999.py
    - ARC
    - etc
  - snuke(???)
    - AGC
      - G
      - EX
