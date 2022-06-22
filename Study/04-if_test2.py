import random

player = int(input("请输入1、2、3（分别代表石头，剪刀，布)"))
computer = random.randint(1, 3)
print("玩家选择的是%d 电脑选择的是%d" % (player, computer))
if player == computer:
    print("平局")
elif (player == 1 and computer == 2) \
        or (player == 2 and computer == 3) \
        or (player == 3 and computer == 1):
    print("玩家获胜")
else:
    print("电脑获胜")
