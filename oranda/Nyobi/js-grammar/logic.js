let age = 16;
let result = null;
let isMember = true;


if (age >= 18) {
  result = '成年';
} else {
  result = '未成年';
}
document.write(result,"で");


if (age >= 60 && isMember) {
  result = 'シニア会員割引の対象です';
} else {
  result = 'シニア会員割引の対象ではありません';
}
document.write(result,"ので");

let num = 3;
if ( num % 3 === 0 ) {
  console.log(`サァン！`);
} else {
  console.log(number);
}

let price = null;
if (age <= 15) {
  price = 800;
} else if (isMember) {
    price = 1000;
} else {
    price = 1800;
}
document.write(price,"円となります。")