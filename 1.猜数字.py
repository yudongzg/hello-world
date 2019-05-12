import random
secret =random.randint(1,100)
times = 3
#print('我心里想的是：'+str(secret))
Gameover = '游戏结束，不玩啦^_^'
print('猜猜我心里想的是哪个数字吧：', end='')
while times:
	times -= 1
	temp = input()
	while not temp.isdigit():
		temp = input('皮！要输入数字哦！重新输入吧：')
	guess = int(temp)
	if guess == secret:
		print('恭喜你猜对啦！')
		break
	else:
		if guess > secret:
			print('诶，不对不对~大啦')
		else:
			print('诶，不对不对~小啦')
		if times != 0:
			print('请重新输入吧：', end='')
		else:
			Gameover = '机会用完了，哼，告辞~'
	
print(Gameover)