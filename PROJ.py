from random import randint
y = 1
v = 0
g = 10
while y:
	print('очки',v)
	print('макс квадрат',g)
	x = randint(g-9, g)
	s = int(input(x**2))
	if s == x:
		v += 1
	if v == g:
		g += 10
	else:
		y = 0