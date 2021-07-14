import random
r = random.randint(1,100) 
i = 0
while True :
	i = i + 1
	num = input('請輸入數字1~100:')
	num = int(num)
	if r == num :
		print('總共猜了', i ,'次')
		print ('終於猜對了!')
		break
	elif r > num :
		print('總共猜了', i ,'次')
		print ('有種再大一點')
	elif r < num :
		print('總共猜了', i ,'次')
		print ('有種再小一點')