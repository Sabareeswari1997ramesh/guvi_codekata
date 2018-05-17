try:

	x=int(raw_input())

	y=int(raw_input())

	z=int(raw_input())

except ValueError:

	print("Enter the integer value only")

else:

	if((x>y)&(x>z)):

		print(x)

	elif((y>x)&(y>z)):

		print(y)

	else:

		print(z)