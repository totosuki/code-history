let game = {
    startTime : null,
    displayArea : document.getElementById('display-area'),

    start : function(){
        game.startTime = Date.now();
        console.log('スタートしました');
    
        document.body.onkeydown = game.stop;
    },

    stop : function(){
        let currentTime = Date.now();
        let seconds = (currentTime - game.startTime) / 1000;
        if (9.5 <= seconds && seconds <= 10.5) {
            game.displayArea.innerText = seconds + '秒でした凄い';
        } else {
            game.displayArea.innerText = seconds + '秒でした残念';
        }
    }
};
if(confirm('OKを押して10秒だと思ったら何かキーを押して下さい')){
    //TODO スタート処理
    game.start();
}

// let catObj = {
//     name: [`茶マル`, `chamalu`],
//     age: 11,
//     feature: `毛並みが茶色くて、丸っこい猫です。`,
//     interests: [`食事`, `昼寝`, `夜の散歩`],
//     bio: function () {
//       console.log(`${catObj.name[0]} は ${catObj.age} 歳の ${catObj.feature}`);
//     },
//     greeting: function() {
//       console.log(`にゃおーにゃおにゃお！（${catObj.interests[0]}と${catObj.interests[1]}が大好きな${catObj.name[0]}だよ！）`);
//     }
// }
// catObj.bio();
// catObj.greeting();