#russel john cortez
#CALCULATOR

while True:
	print("1.Add")
	print("2.Subt")
	print("3.Multiply")
	print("4.Divide")
	print("5.Exit")
	choice=int(input("Enter your choice:"))
	if (choice>=1 and choice<=4):
		print("Enter two numbers:")
		num1=int(input())
		num2=int(input())
		if choice == 1:
			res = num1+num2
			print("Result =", res)
		elif choice == 2:
			res = num1-num2
			print("Result =", res)
		elif choice == 3:
			res = num1*num2
			print("Result =",res)
		else:
			res = num1/num2
			print("Result =",res)
	elif choice ==5:
		break
	else:
		print("Invalid input!")
