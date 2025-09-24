import random
import time

property = 1000
while(property > 0):
    print(f'你现在拥有的财产为:{property}')
    bet = int(input("请选择下注的金额:"))
    if bet > property:
        print("你的余额不足！！！")
        continue
    
    print("现在进行第1次投掷...")
    a = random.randrange(1, 7)
    print(f'第一个骰子点数为 {a}')
    time.sleep(1)
    b = random.randrange(1, 7)
    print(f'第二个骰子点数为 {b}')
    time.sleep(1)
    c = a + b
    print(f'点数之和为 {c}')
    time.sleep(1)
    print()

    if c == 7 or c  == 11:
        print(f'玩家胜！获得奖励:{bet}！')
        property += bet
        time.sleep(2)
        print()
        continue
    elif c == 2 or c == 3 or c == 12:
        print(f'庄家胜！玩家输掉赌注:{bet}！')
        property -= bet
        time.sleep(2)
        print()
        continue
    
    times = 2
    while True:
        print(f'现在进行第{times}次投掷...')
        a = random.randrange(1, 7)
        print(f'第一个骰子点数为 {a}')
        time.sleep(1)
        b = random.randrange(1, 7)
        print(f'第二个骰子点数为 {b}')
        time.sleep(1)
        d = a + b
        print(f'点数之和为 {d}')
        time.sleep(1)
        print()

        if d == 7:
            print(f'庄家胜！玩家输掉赌注:{bet}！')
            property -= bet
            time.sleep(2)
            print()
            break
        elif d == c:
            print(f'玩家胜！获得奖励:{bet}！')
            property += bet
            time.sleep(2)
            print()
            break
        times += 1
    
    continue

print("你破产了！！！游戏结束...")