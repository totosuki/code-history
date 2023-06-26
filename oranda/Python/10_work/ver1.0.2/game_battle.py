#インポート
import random 
import math
import time
import sys
import os
import game_main

bos = 0
# コンソール綺麗君改

def delete_lines(num):
    # ターミナルのn行分の長さを取得
    cursor_up_n = '\x1b[{}A'.format(num)
    erase_line = '\x1b[2K'
    sys.stdout.write(cursor_up_n)
    for _ in range(num):
        sys.stdout.write(erase_line)

# 初代
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

# ===== 定数 ===== #
atk_rate = 2
defense_rate = 3

#努力値(同じレベルの敵を何回倒せばレベルが上がるのか？の定数)
effort_value = 4
#基準値？初期値
initial_xp = 8
#経験値レベル毎の差
xp_rate = 2

# ステータス最低保証値
min_current_hp = 0
min_max_hp = 0
min_attack = 0
min_defense = 0

# 討伐数カウンター
kill_count = 0

#self.player.xp += initial_xp / effort_value * (xp_rate ** (self.enemy.lv - 1))
#敵lv(N)を倒した時の経験値 = 基準値 / 倒さなきゃいけない同lvの敵の数 * ( 倍率(A)謎い ** (敵のlv(N) -1) )

# 役職
class job:

    def __init__(self,name,max_hp,speed,attack,defense):
        #名前
        self.name = name
        #最大HP
        self.max_hp = max_hp
        #初期スピード値
        self.speed = speed
        #攻撃力
        self.attack = attack
        #防御力
        self.defense = defense



# スキル親クラス
class Skill:

    def __init__(self, name, cool):
        self.name = name
        #スピード減少値
        self.cool = cool


# スキル_ダメージ
class Skill_damage(Skill):

    def __init__(self,name,atk,rate,cool):
        
        super().__init__(name, cool)

        #ダメージ倍率
        self.atk = atk
        #クリティカルダメージ...倍率？(一旦)
        self.critical = 1.3
        #クリティカル率
        self.rate = rate


# 代償スキル(self harmから)
class Skill_self(Skill):

    def __init__(self,name,atk,rate,leave,adjust,cool):
        
        super().__init__(name, cool)

        #ダメージ倍率
        self.atk = atk
        #クリティカルダメージ...倍率？(一旦)
        self.critical = 1.3
        #クリティカル率
        self.rate = rate
        #代償値
        self.leave = leave
        #調整値
        self.adjust = adjust



# スキル_チェンジ(クソコード)
class Skill_change(Skill):
    def __init__(self,name,cool):
        super().__init__(name, cool)

        
# スキル_エフェクト(バフとか？)
class Skill_effect(Skill):

    def __init__(self,name,type,strength,turn,cool):
        super().__init__(name, cool)

        #エフェクトタイプ
        self.type = type
        #効果値
        self.strength = strength
        #効果ターン
        self.turn = turn


class Effect:
    
    def __init__(self, type, strength, turn):
        # タイプ
        self.type = type
        # 効果値
        self.strength = strength
        # 持続ターン
        self.turn = turn
        


# エネミークラス
class Enemy:

    #プレイヤーの基本ステータスを定義します
    def __init__ (self,name,current_hp,xp):
        #名前
        self.name = name
        #現在HP
        self.current_hp = current_hp 
        #経験値
        self.xp = xp
        #レベル
        self.lv = 1
        #役職
        self.job = None
        # 役職dict {job.name : job}
        self.jobs = {}
        #スキルボックス
        self.skills = []
        #エフェクトボックス
        self.effect = []
        #現在speed
        self.current_speed = 0
        

    # スキル追加メソッド
    def append_skills(self,skills: list):
        for skill in skills:
            self.skills.append(skill)

    # 役職追加メソッド
    def append_jobs(self, jobs: list[tuple]):
        for job_data in jobs:
            self.jobs.update({job_data[0] : job_data})


    #　状態異常追加メソッド
    def append_effect(self, effect : Effect):
        self.effect.append(effect)


    # 役職変更メソッド
    def set_job(self, job_name):
        # 役職を持っているか確認
        if job_name not in list(self.jobs.keys()):
            print("その役職はありません")
            return
        
        # 役職を設定
        self.job : job = job(*self.jobs[job_name])
        # HPの最大値を調整
        if self.current_hp > self.job.max_hp * self.lv + min_max_hp:
            self.current_hp = self.job.max_hp * self.lv + min_max_hp
        

    # 回復メソッド
    def heal(self,amount):
        self.current_hp += amount
        if self.current_hp > self.job.max_hp * self.lv + min_max_hp:
                self.current_hp = self.job.max_hp * self.lv + min_max_hp
        print(self.name,"は回復した")
        print(self.name,"のHPは",self.current_hp)

    # effect_clearメソッド
    def effect_clear(self):
        self.effect.clear()

    # 次のレベルに必要な経験値
    def lv_update(self,get_xp = 0):
        if get_xp == 0:
            while self.xp >= self.lv**2 * 5:
                self.lv += 1
            self.heal(self.job.max_hp * self.lv + min_max_hp)
        else:
            get_xp = (get_xp**2 * 5) / 3
            print(f"{get_xp}xp獲得")
            self.xp += get_xp
            while self.xp >= self.lv**2 * 5:
                self.lv += 1
                self.heal(self.job.max_hp * self.lv + min_max_hp)
                print("レベルアップ！")

            next_xp = self.lv**2 * 5 - self.xp
            print(f"現在のレベルは{self.lv}")
            print(f"次のレベルに必要な経験値は{next_xp}")

# プレイヤークラス
class Player(Enemy):

    # プレイヤーの基本ステータスを定義します
    def __init__ (self, name, current_hp, xp):
        # 継承
        super().__init__(name, current_hp, xp)

    # 回復メソッド
    def heal(self,amount):
        self.current_hp += amount
        if self.current_hp > self.job.max_hp * self.lv + min_max_hp:
                self.current_hp = self.job.max_hp * self.lv + min_max_hp
        print(self.name,"は回復した")
        print(self.name,"のHPは",self.current_hp)

# バトルクラス
class Battle:

    # 引数にプレイヤーとエネミーを入れる
    def __init__(self,player,enemy):

        self.player = player
        self.enemy = enemy
        self.battle_speed = 0
        
    # 状態異常を確認するメソッドです
    def Check_effect(self,user):
        i = 0
        while i < len(user.effect):
            # 状態異常があればturn-1
            if(len(user.effect) > 0):
                user.effect[i].turn -= 1

            print(f"{i}番目の状態異常の残りのターン数は{user.effect[i].turn}です")

            # ここに状態異常の種類を追加する
            
            # 毒の処理
            if user.effect[i].type == "poison":
                if 1 > (user.current_hp / 100 ) * user.effect[i].strength:
                    user.current_hp -= 1
                else:
                    user.current_hp -= (user.current_hp / 100 ) * user.effect[i].strength

            # 死の宣告
            if user.effect[i].type == "death_sentence":
                if user.effect[i].turn <= 0:
                    user.current_hp -= user.current_hp 
                    break

            # 恐怖
            if user.effect[i].type == "fear":
                user.job.attack -= (user.job.attack / 100) * user.effect[i].strength
                if user.effect[i].turn <= 0:
                    user.job.attack += (user.job.attack / 100) * user.effect[i].strength

            # 出血
            if user.effect[i].type == "bleeding":
                user.current_hp -= ((user.lv * user.job.max_hp)  / 100 ) * user.effect[i].strength 

            # 共感覚(痛み分け？)
            if user.effect[i].type == "share":
                user.current_hp -= (user.lv * user.job.attack)* user.effect[i].strength / 2

            # 炎
            if user.effect[i].type == "flame":
                count = 0
                while True:
                    if user.effect[i].type == "flame":
                        count += user.effect[i].strength
                    if i < len(user.effect):
                        break
                user.current_hp -= count * user.job.attack / 2.5
                
                
            # 表示処理
            if(len(user.effect) > 0):
                print(user.name,"は",user.effect[i].type,"状態です","現在HPは",user.current_hp)

            #スキル削除処理
            if(user.effect[i].turn <= 0):
                print(f"{i}番目のスキルの{user.effect[i].type}状態は解消されました")
                del user.effect[i]

            i += 1



        # for i in range(len(user.effect)):
        #     # 状態異常があればturn-1
        #     if(len(user.effect) > 0):
        #         user.effect[i].turn -= 1

        #     print(f"{i}番目のスキルの残りのターン数は{user.effect[i].turn}です")

        #     # ここに状態異常の種類を追加する
            
        #     # 毒の処理
        #     if user.effect[i].type == "poison":
        #         user.current_hp -= (user.current_hp / 100 ) * user.effect[i].strength 

        #     # 死の宣告
        #     if user.effect[i].type == "death_sentence":
        #         if user.effect[i].turn <= 0:
        #             user.current_hp -= user.current_hp 
        #             break

        #     # 恐怖
        #     if user.effect[i].type == "Fear":
        #         user.job.attack -= (user.job.attack / 100) * user.effect[i].strength
        #         if user.effect[i].turn <= 0:
        #             user.job.attack += (user.job.attack / 100) * user.effect[i].strength

        #     # 表示処理
        #     if(len(user.effect) > 0):
        #         print(user.name,"は",user.effect[i].type,"状態です","現在HPは",user.current_hp)

        #     #スキル削除処理
        #     if(user.effect[i].turn <= 0):
        #         print(f"{i}番目のスキルの{user.effect[i].type}状態は解消されました")
        #         del user.effect[i]

        # # 削除処理(一週目で削除してしまうと他のindexが変わる事を恐れて)
        # for i in range(len(user.effect)):
        #     if user.effect[i].turn <= 0:
        #         print(user.effect[i].type,"状態は解消されました")
        #         del user.effect[i]



    # バトルの流れ    
    def main(self):
        # self.player.next_lv()

        # スピードの初期値を設定
        self.player.current_speed += self.player.job.speed * self.player.lv / 100
        self.enemy.current_speed += self.enemy.job.speed * self.enemy.lv / 100
        self.battle_speed += (self.player.job.speed * self.player.lv + self.enemy.job.speed * self.enemy.lv) / 4

        print(self.enemy.name,"のHP",
                self.enemy.current_hp,
            "atk",min_attack + (self.enemy.job.attack * self.enemy.lv ),
            "def",(min_defense + (self.enemy.job.defense * self.enemy.lv))/defense_rate)
        print(self.player.name,"のHP",
                self.player.current_hp,
            "atk",min_attack + (self.player.job.attack * self.player.lv ),
            "def",(min_defense + (self.player.job.defense * self.player.lv))/defense_rate)
        


        # 攻撃回数を記録する変数
        player_atk_count = 0
        enemy_atk_count = 0
        print(f"レベル{self.enemy.lv}の{self.enemy.name}が現れた！")
        
        time.sleep(1)
        order = 0
        # どちらかのスピードが100になるまで繰り返す
        while(True):
            # お互いのスピードを１ずつ足してる
            self.enemy.current_speed += 1
            self.player.current_speed += 1
            #バトルターンのカウント
            
            self.battle_speed += 1

            if(self.battle_speed >= 50):
                self.Check_effect(self.enemy)
                self.Check_effect(self.player)
                self.battle_speed = 0

            # 攻撃可能かのif文(条件の100に達しているのかどうか)
            if(self.enemy.current_speed >= 100):
                if(self.enemy.current_hp <= 0):
                    break
                else:
                    enemy_atk_count += 1
                    print(f"\n{self.enemy.name}のターン")
                    # Calculate_Damageの引数には、ダメージを受ける人と攻撃側の攻撃力が入る
                    self.Calculate_Damage(
                        self.player,
                        # Calculate_atkの引数には攻撃の使用者と、減らすspeedが誰のなのかと、どのスキルを使うのかが入る
                        self.Calculate_atk(
                            self.enemy,
                            # スキルをランダムにする)
                            order,
                            self.player
                            ))
                    if(order < len(self.enemy.skills) - 1):
                        order += 1
                    else:
                        order = random.randint(0,len(self.enemy.skills) - 1)

            if(self.player.current_speed >= 100):
                if(self.player.current_hp <= 0):
                    break
                else:
                    player_atk_count += 1
                    print("")
                    print(self.player.name,"のターン")
                    print("使いたいスキルのindex番号を入力してください",len(self.player.skills),"個が現在使えるスキルの数です。")
                    num = input()
                    # Calculate_Damageの引数には、ダメージを受ける人と攻撃側の攻撃力が入る
                    self.Calculate_Damage(
                        self.enemy,
                        # alculate_atkの引数には攻撃の使用者と、減らすspeedが誰のなのかと、どのスキルを使うのかが入る(使いたいスキルのindexがinputに入る)
                        self.Calculate_atk(
                            self.player,
                            int(num),
                            self.enemy
                            ))

            if(self.player.current_hp <= 0):
                break       
            elif(self.enemy.current_hp <= 0):
                break

        if(self.player.current_hp <= 0):
                    print(self.player.name,"の負け")
                    print("プレイヤーは",player_atk_count,"回攻撃しました")
                    print("プレイヤーは",enemy_atk_count,"回攻撃されました")
                         
        elif(self.enemy.current_hp <= 0):
            print(self.enemy.name,"の負け")
            time.sleep(1)
            self.player.lv_update(self.enemy.lv)
            # print(int(self.player.xp),"経験値")
            
            print("プレイヤーは",player_atk_count,"回攻撃しました")
            print("プレイヤーは",enemy_atk_count,"回攻撃されました")
            
        
        
    # ダメージ計算を行うメソッドです(引数には攻撃側の合計攻撃力が入ります)
    def Calculate_Damage(self,user,Attack):
        if(Attack > 0):
            # ダメージ計算式(ダメージ = 攻撃÷攻撃軽減率 - 防御力÷防御軽減率)
            damage = math.floor((Attack/atk_rate) - ((min_defense + (user.job.defense * user.lv))/defense_rate))
            # 現在HPをダメージ分減らしている
            if damage > 0:
                user.current_hp -= damage
                print(user.name,"に",damage,"ダメージ！！")
            else:
                print(user.name,"に",0,"ダメージ！！")
            print(user.name,"のHPは",user.current_hp)
        
    # 攻撃計算を行うメソッドです(引数indexにはスキルのindexが入る)
    def Calculate_atk(self,user,index,target):

        skill = user.skills[index]
        print(skill.name)
        user.current_speed -= skill.cool
            
        if isinstance(skill, Skill_damage):
            # クリティカル計算(率とダメージ)
            if(skill.rate >= random.randint(1,100)):
                # min_attackはゲーム性の為にある最低保証みたいなもん
                print("critical！")
                return min_attack + (user.job.attack * user.lv * user.skills[index].atk * user.skills[index].critical)
            else:
                return min_attack + (user.job.attack * user.lv * user.skills[index].atk)
            
        elif isinstance(skill, Skill_change):
            print("変更したい役職の名前を入力してください")
            job_name = input()
            user.set_job(job_name)
            return 0

        elif isinstance(skill, Skill_effect):
            if skill.type == "heal":
                user.heal(user.job.max_hp * user.lv / 100 * skill.strength)

            elif skill.type == "clear":
                user.effect_clear()
            
            else:
                effect = Effect(skill.type, skill.strength, skill.turn)
                target.append_effect(effect)
            return 0
        
        elif isinstance(skill, Skill_self):
            if user.current_hp >= 50:
                power = 0
                power += user.current_hp
                user.current_hp = (user.current_hp + skill.leave) - user.current_hp
                power = power - user.current_hp
            else:
                power = 0
                power += user.current_hp
                user.current_hp = user.current_hp - user.current_hp
                power = power - user.current_hp
            print("消費したHP",power)
            
            if(skill.rate >= random.randint(1,100)):
                # min_attackはゲーム性の為にある最低保証みたいなもん
                print("critical！")
                print()
                return min_attack + (user.job.attack * user.lv * user.skills[index].atk * user.skills[index].critical ) * (1 + (power/1000)**3) + skill.adjust
            else:
                return min_attack + (user.job.attack * user.lv * user.skills[index].atk) * (1 + (power/1000)**3) + skill.adjust
                



def main():
    # ===== スキル ===== #
    # 名前,スピード減少値
    # 特殊換装スキル、獲得条件なし(最初の敵を倒してからかも)
    s = Skill_change("クラスチェンジ",60)

    # ===== 汎用型スキル ===== #
    # 名前,ダメージ倍率,クリティカル率,スピード減少値
    # 条件なし
    s_1 = Skill_damage("スラッシュ",1,20,90)
    # 条件(スラッシュをn回使うとか)
    s_2 = Skill_damage("スイフトスラッシュ",1,0,77)

    # 条件(攻撃をされること)
    es_1 = Skill_damage("突進",1,35,130)
    # 条件(不可)
    es_2 = Skill_damage("切り裂く",1.1,40,140)
    # 条件(蛇を倒す事)
    es_3 = Skill_effect("シャドウファング","poison",4,10,50)

    # 条件(騎士を獲得すること？)
    es_4 = Skill_damage("パラディンスマイト",1.1,65,100)

    # 条件(強すぎるので後々)
    es_5 = Skill_effect("エンチャントファイア","flame",1,3,40)

    # 条件()
    es_6 = Skill_effect("アサシネイト","death_sentence",1,5,90)

    # 条件()
    es_7 = Skill_effect("クイックヒール","heal",20,0,60)

    # 条件()
    es_9 = Skill_effect("フェアリーキュア","clear",0,0,100)

    # 条件()
    es_10 = Skill_damage("インフェルノ",1.2,55,180)

    # 条件()
    es_11 = Skill_damage("ボルトショット",0.8,30,40)

    # 条件()
    es_12 = Skill_effect("威圧","fear",8,3,80)

    # 条件()
    es_13 = Skill_effect("ポイズンボム","poison",12,6,90)

    # 条件()
    es_14 = Skill_damage("ハンティングボウ",0.9,25,45)

    # 条件()
    es_15 = Skill_effect("ロング・トルメント","poison",3,30,50)

    # 条件()
    es_16 = Skill_effect("ヴェノム・ストライク","poison",65,2,90)

    # 条件()


    # 条件()
    es_18 = Skill_self("ギフト",0.96,0,0,0,0,)




    # 名前,ダメージ倍率,クリティカル率,残すHP,調整値,スピード減少値
    # 代償スキル、条件なし(レベル10を超えるとダメージバグり始める)
    f_1 = Skill_self("ラストリゾート",1.2,0,1,51,2000)

    # エフェクトタイプ,効果値,ターン数,スピード減少値
    # 状態変化スキル、条件
    s_3 = Skill_effect("ポイズンミスト","poison",10,4,0)

    s_5 = Skill_damage("ピアシングストライク",1.6,40,85)
    s_6 = Skill_damage("タイタンブレード",1.8,10,170)
    s_7 = Skill_damage("ソウルスティール",1,0,250)

    # エフェクトタイプ,効果値,ターン数,スピード減少値
    s_4 = Skill_effect("クイックヒール","heal",40,0,21)
    s_5 = Skill_effect("リジェネレーション","heal",100,0,100)
    s_8 = Skill_effect("ナイトメアレスト","heal",200,0,260)
    s_9 = Skill_effect("宿屋","heal",200,0,0)

    s_10 = Skill_effect("死の宣告","death_sentence",None,2,0)

    #player_skills = [s,s_1,s_2,f_1, s_3, s_4, s_5, s_6,s_7,s_8,s_10]
    player_skills = [s,s_1]

    # ===== 役職 ===== #
    # job(最大HP,初期スピード値,攻撃力,防御力)
    # プレイヤー役職
    normal_jobs = [
        ("ルーキー",100,100,100,100),
        ("猪",100,100,100,65),
        ("熊",110,105,120,70),
        ("蛇",10,130,100,40),
        ("騎士",115,75,105,120),
        ("エンチャンター",105,400,10,50),
        ("暗殺者",105,120,105,90),
        ("魔術師",105,85,135,65),
        ("スライムハンター",135,106,105,90),
        ("ヴェノムスパイダー",115,106,0,115),
        ("アビスハウラー",120,115,110,75),
        ("ギフテッド",77,125,77,77),
    ]

    player_jobs = normal_jobs 

    enemy_list = [
        # 森編
        ["猪",1,1,normal_jobs[1],[es_1]],
        ["熊",1,1,normal_jobs[2],[es_1,es_2]],
        ["蛇",1,1,normal_jobs[3],[es_3]],

        # ギルド試験
        ["試験相手",1,5,normal_jobs[0],[es_3,es_3,s_1,s_1,s_1,s_1]],

        # 二階編
        ["スライムナイト",1,5,normal_jobs[4],[s_2,es_4,]],
        ["スライムエンチャンター",1,5,normal_jobs[5],[es_5]], 
        ["アサシンスライム",1,5,normal_jobs[6],[es_6,es_7]],
        ["スライムウィザード",1,5,normal_jobs[7],[es_10,es_11,es_11,es_11,es_11]],
        ["スライムハンター",1,5,normal_jobs[8],[es_12,es_13,es_14,es_7]],

        # 洞窟編
        ["ヴェノムスパイダー",1,15,normal_jobs[9],[es_15,es_16,es_11]],
        ["アビスハウラー",1,15,normal_jobs[10],[]],
        ["ギフテッド",1,15,normal_jobs[11],[es_16]],
    ]

    # プレイヤーをを作成
    # 名前,現在HP(いらんかも),経験値
    player = Player("もも",1,60)
    # ステータスを設定
    player.append_jobs(player_jobs)
    player.append_skills(player_skills)
    player.set_job("ルーキー")
    player.lv_update()
    clear_console()

    def e_ran():
        global bos
        if player.lv > 10:
            return random.randint(9,11)
        elif player.lv > 6:
            if bos < 1:
                bos += 1
                return 3
            else:
                return random.randint(4,8)
        else:
            return random.randint(0,2)
    
    def ramn():
        return random.randint(player.lv-2,player.lv+2)

    def start_battle():
        def create_enemy():
            # ランダムに敵を作成
            n = e_ran()

            #enemyのlvを作成
            e_xp = 0
            ram = ramn()
            if ram < 1:
                ram = 1


            for i in range(ram):
                e_xp += i**2 * 5

            # 名前,現在HP,経験値
            e = Enemy(enemy_list[n][0],enemy_list[n][1],e_xp)
            e.job = job(*enemy_list[n][3])
            e.append_skills(enemy_list[n][4])
            e.lv_update()
            delete_lines(2)
            return e

        # バトルをする
        enemy = create_enemy()
        b = Battle(player, enemy)
    
        b.main()
        
        # プレイヤーが生きていれば次のバトルを開始
        if player.current_hp > 0:
            global kill_count
            kill_count += 1
                
            start_battle()

    start_battle()

    time.sleep(0.5)
    # 終了処理
    print("これでゲーム終了です。")

    # 討伐数に応じたリザルトを表示
    if(kill_count <= 5):
        time.sleep(0.2)
        print(f"討伐数は{kill_count}匹でした")
        time.sleep(0.3)
        print("次はもっと頑張ってください！")

    elif(kill_count > 10):
        time.sleep(0.2)
        print(f"討伐数はな、なんと{kill_count}匹でした！！")
        time.sleep(0.3)
        print("お見事！！")

    else:
        time.sleep(0.2)
        print(f"討伐数はなんと{kill_count}匹でした！")
        time.sleep(0.3)
        print("お疲れ様でした！")

main()