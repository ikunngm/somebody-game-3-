import random
import time
from 血量与金币 import*
from 技能 import*
from colorama import Fore,Back,init
init(autoreset=True)
print (Back.WHITE+Fore.BLACK+'恶魔之城？黑气笼罩，似乎是个不吉之地......\n魔王奴役着人民，他们需要你!\n别害怕,坤坤会用唱跳Rap和篮球助你一臂之力!\n出发吧,圣骑士!一定要活着回来！/开始(Enter)' ) 
# 游戏循环
while True:
    while True:    
        # 金币随机增加
        coin += random.randint(coin_scopes[0], coin_scopes[1])
        # 减少道具冷却   
        if basketball_time > 0:
            basketball_time -= 1
        else:
            basketball_time = 0 
        if ctr_time > 0 :
            ctr_time -= 1
        else:
            ctr_time = 0 
        if jlq_time > 0:
            jlq_time -= 1
        else:
            jlq_time = 0 
        # 随机暴击    
        crit = random.randint(1, int(1/crit_rate))  
        # 攻击
        put = input()
        if put == '':
            if crit == 1:
                king_xp -=2*attack 
            else:king_xp -= attack
        # 控制 
        if crit == 1:        
            print('暴击!') 
        if put=='':   
            print('魔王血量还有' + str(king_xp),',你的血量还有'+ str(you_xp),',金币剩余' + str(coin), '/攻击(Enter)/进入商店(B)/使用道具(I)/尝逝逃跑(X)')    
        #伤害
        if king_xp<=1000 and put=='':   
            #随机扣血   
            jj = random.randint(1, int(1/jj_rate))  
            if jj == 1:
                you_xp -= hurt    
        # 商店
        elif put == 'B' or put == 'b':
            while True:
                print(Fore.BLUE+'商店，金币剩余' + str(coin))
                print(basketball, '/购买(1)')
                print(ctr,'/购买(2)')
                print(jlq,'/无需购买')
                print('选择你要购买的商品吧/离开商店(X)')
                put_shop = input()
                if put_shop == '1':
                    if basketball_state == 0:
                        if coin >= 1000:
                            coin -= 1000
                            basketball_state += 1
                            print(Fore.YELLOW+'购买成功')
                        else:
                            print(Fore.RED+'你是想白嫖吗?')
                    else:
                        print(Fore.RED+'做人不要太贪心')
                if put_shop == '2':
                    if ctr_state == 0:
                        if coin >=1500:
                            coin -= 1500
                            ctr_state += 1
                            print(Fore.YELLOW+'购买成功')
                        else:
                            print(Fore.RED+'你是想白嫖吗?')
                    else:
                        print(Fore.RED+'做人不要太贪心')
                elif put_shop == 'X' or put_shop == 'x':
                    print('离开商店')
                    break
        #技能
        elif put == 'I' or put == 'i':
            while True:
                if basketball_state == 0 and ctr_state == 0:
                    print(Fore.RED+'你是想白嫖吗?你还没有买技能呢/退出(X)')
                if basketball_state == 1 or ctr_state == 1 or jlq_time==1:
                    print(Fore.BLUE+'技能，金币剩余' + str(coin))
                    print(basketball, '冷却剩余(' + str(basketball_time), ')/发动(1)')
                    print(ctr,'冷却剩余(' + str(ctr_time), ')/发动(2)')
                    print(jlq,'冷却剩余(' + str(jlq_time), ')/发动(3)') 
                    print('选择你要使用的道具吧/取消使用(X)')
                put_prop = input()
                # 篮球
                if put_prop == '1':
                    if basketball_state==0:
                        print(Fore.RED+'你还没买篮球呢！')
                    if basketball_time == 0 and basketball_state == 1: 
                        # 道具'篮球'（-50）
                        print(Fore.GREEN+str(king_xp) + '-10')
                        print(Fore.GREEN+str(king_xp) + '-10')
                        print(Fore.GREEN+str(king_xp) + '-10')
                        print(Fore.GREEN+str(king_xp) + '-10')
                        print(Fore.GREEN+str(king_xp) + '-10')
                        king_xp -= 50
                        basketball_time = 5
                    else:
                        print(Fore.YELLOW+'还没冷却完成，再等等吧')
                elif put_prop == 'X' or put_prop == 'x':
                    print('取消使用')
                    break
                #唱跳RAP
                if put_prop == '2':
                    if ctr_state==0:
                        print(Fore.RED+'你还没买唱跳Rap呢！')   
                    if ctr_time == 0 and ctr_state == 1:
                        # 道具'唱跳Rap'（-105）
                        print(Fore.GREEN+str(king_xp) + '-5')
                        print(Fore.GREEN+str(king_xp) + '-10')
                        print(Fore.GREEN+str(king_xp) + '-15')
                        print(Fore.GREEN+str(king_xp) + '-20')
                        print(Fore.GREEN+str(king_xp) + '-25')
                        print(Fore.GREEN+str(king_xp) + '-30')
                        king_xp -= 105
                        ctr_time = 15
                    else:
                        print(Fore.YELLOW+'还没冷却完成，再等等吧')
                elif put_prop == 'X' or put_prop == 'x':
                    print('取消使用')
                    break    
                #减冷却
                if put_prop=='3':
                    if ctr_state==1:  
                        if jlq_time==0:
                            if ctr_time==15:  
                                if coin>=50:
                                    coin-=50 
                                    ctr_time-=15
                                    jlq_time=50
                                    print(Fore.YELLOW+'减冷却成功！')
                                else:
                                    print(Fore.RED+'你是想白嫖吗?')           
                            else:
                                print(Fore.RED+'好人做到底，唱跳RAp的冷却点数不足15，下次再逝吧')    
                        else:
                            print(Fore.YELLOW+'还没冷却完成，再等等吧') 
                    else:
                        print(Fore.RED+'你还没买唱跳Rap呢！')                                                
                elif put_prop == 'X' or put_prop == 'x':
                    print('取消使用')
                    break    
        # 逃跑 
        if put == 'X' or put == 'x':
            print(Back.RED+'胆小鬼，你逃离了恶魔之城，你连攻击都不会吗?真的太逊了')   
            break
        # 战胜
        if king_xp <= 0:   
            print(Fore.YELLOW+'英雄，你战胜了魔王!!!')
            break
        #你死了
        if you_xp <= 0: 
            print(Fore.RED+'你死了')            
            break
    time.sleep(5)
    break