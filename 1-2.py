from random import randint

for y in range(200):
	rlt=0
	for x in range (2):
		rlt=rlt+randint(1,8)
		
	print(rlt,end=" ")