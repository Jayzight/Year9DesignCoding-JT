#Input
num1 = input("")
num1 = int(num1)
num2 = input("")
num2 = int(num2)

num3 = input("")
num3 = int(num3)
num4 = input("")
num4 = int(num4)

if num1 == 8 or num1 == 9:
	if num2 == num3:
		if num4 == 8 or num1 == 9:
			print ("ignore")
		else:
			print("answer")
	else:
		print("answer")
else:
	print("answer")
