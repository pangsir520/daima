for number in range(1,101):
	if number%7==0 or number%10==7 or number//10==7:
		continue
	else:
		print(number)
