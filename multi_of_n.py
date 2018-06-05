try:

    n=int(raw_input())

except ValueError:

    print("Enter only integers")

else:

    for i in range(1,6):

    	print(n*i)