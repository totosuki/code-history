// let myBirthTime = new Date('2005-06-16 12:30');
// function updateParagraph() {
//   let now = new Date();
//   let seconds = (now.getTime() - myBirthTime.getTime()) / 1000;
//   document.getElementById('birth-time').innerText =
//     '生まれてから' + seconds + '秒経過。';
// }
// setInterval(updateParagraph, 50);

// function areaOfCircle(r) {
//   let area = r * r * Math.PI;
//   return area;
// }
// document.write('<p>半径 5cm の円の面積は ' + areaOfCircle(5) + 'です。</p>');
// document.write('<p>半径 10cm の円の面積は ' + areaOfCircle(10) + 'です。</p>');
// document.write('<p>半径 15cm の円の面積は ' + areaOfCircle(15) + 'です。</p>');

// function collatz(n) {
//   document.write("nは",n,"です<br>")
//   if (n === 1){
//     document.write("end")
//   }else if (n % 2 === 0) {
//     collatz(n / 2);
//   }else{
//     collatz((n * 3)+1)
//   }
// }
// collatz(99999999997)

function reply(){
  document.write("わかりました。頑張ります")
  reply()
}
reply()