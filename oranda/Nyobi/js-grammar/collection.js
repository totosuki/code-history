// let classes = ['A組', 'B組', 'C組', 'D組'];
// for (let grade = 1; grade <= 3; grade++) {
//     for (let i = 0; i < classes.length; i++) {
//         document.write(grade + '年' + classes[i],'<br>');
//     }
// }

// let scores = [23, 56, 78, 33, 78, 20, 55, 67, 78];
// let maxScore = 0;
// for (let i = 0; i < scores.length ; i++) {
//   if (maxScore < scores[i]) {
//     maxScore = scores[i];
//   }
// }

// document.write('最高得点は' + maxScore + '点 です！');
// document.write(`最高得点は ${Math.max(...scores)}点 です！`);

let chars = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ'];
for (let i = 0; i < chars.length; i++) {
  for (let j = 0; j < chars.length; j++) {
    document.write('<p>' + chars[i] + chars[j] + '</p>');
  }
}