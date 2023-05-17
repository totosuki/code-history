# code-history
## code-historyとは？
過去に書いたコード（付随する`.txt`,`.json`等も可）をアーカイブ的にまとめたリポジトリ。
## code-hitosryの使い方
世界一簡単です。<br>
Cloneしたローカルリポジトリに、アーカイブ化したいファイルをぶち込むだけ!!
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
- `.gitignore`はいじらないでね！！
- 個人情報は乗らないように気をつけよう。(絶対パスやトークン、メールアドレスなど)
- パスが入ってるコードは`path/to/hoge.csv`などに変更するの推奨。
- `.ipynb`は可能な限り出力結果を消してからアーカイブ化して下さい。(出力結果によってはファイルサイズやばくなるよ)
