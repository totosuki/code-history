let before = 1000000;
let mul = 1.06 ** 10;
let after = before * mul;
let answer = after - before;
document.write(answer,"<br>");

// このコードは三角形の面積を求めるプログラムです。
let w = 3; // 三角形の底辺
let h = 10; // 三角形の高さ
let area = (w * h) / 2; // 三角形の面積の公式「（底辺）×（高さ）÷2」を使って計算し、areaという名前の変数に代入する
document.write("面積は",area,"<br>"); // 面積を出力する

// お会計
let tax = 10;
let price = 290;
let tax_included = price + (price / 100 * 10)

document.write(tax_included,"円です。<br>")

let r = 12;
let pi = Math.PI
document.write("円の面積は",r*r*pi,"<br>")