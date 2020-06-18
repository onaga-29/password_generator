import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890@#%&*!?^$ABCFHFEEHUNQROPRUIYTZM'
while True:
	np=int(input("How many password: "))
	lp=int(input("Length of each: "))
	for i in range(np):
		psswrd=''
		for j in range(lp):
			rchr=random.choice(chars)
			psswrd+=rchr
		print(psswrd)
