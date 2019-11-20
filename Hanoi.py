def hanoi(n,a,b,c):
	if n>0:
		hanoi(n-1,a,c,b)	#把第n-1个盘子从a 经过 b 挪到 c
		print("#%d: moving form %s to %s." %(n, a, c))  #把第n-1个盘子从a 挪到 c
		hanoi(n-1,b,a,c)    #把n-1个盘子从b 经过a 挪到c

		"""
		n: 问题规模
		a: 起始盘子
		b: 路过盘子
		c: 目标盘子
		"""
hanoi(2, 'a', 'b', 'c')
print('\n')
hanoi(3, 'a', 'b', 'c')

#The times of the movement of hanoi is h(x)=2h(x-1)+1.   h(x)=(2^x)-1

