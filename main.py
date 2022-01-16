import time
import random

print('无聊的积分小游戏')
print('允许使用图色脚本，但请勿使用内存 hook 等外挂手段')
start = time.time()
points = 0
while (time.time() - start) < 60:
    if random.random() < 0.5:
        ch = input('要增加分数么？输入 Y 增加，否则减少\n')
        if (ch == 'Y'):
            points += 1
    else:
        ch = input('要增加分数么？输入 Y 减少，否则增加\n')
        if (ch == 'Y'):
            points -= 1

print(f'游戏结束！你的最终分数为{points}！')
