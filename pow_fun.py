try:

	x=int(raw_input())

	y=int(raw_input())

except ValueError:

	print("enter the integers only")

else:

	print(pow(x,y))