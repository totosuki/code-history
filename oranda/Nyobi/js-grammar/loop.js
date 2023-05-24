for(let i=10;i >= 0;i--){
    document.write("遠足まであと",i,"日<br>")
}

let result
for(let i=1;i<=100000;i++){
    if((i % 3 === 0) && (i%5===0)){
        result = "FizzBuzz"
    }else if(i%3===0){
        result = "Fizz"
    }else if(i%5===0){
        result = "Buzz"
    }else{
        result = i
    }
    document.write(result + " ")
}