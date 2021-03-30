count=0
number=10
while count<number:
	print("输入华氏温度：")
	hua=float(input())
	C=(hua-32)/1.8
	print("华氏温度是{},摄氏温度是{}".format(hua,C))
