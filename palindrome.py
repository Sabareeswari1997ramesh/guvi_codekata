try:

    x=int(raw_input())

except ValueError:

    print("Enter the integer only")

else:

    y=str(x)

    z=y[::-1]

    if(y==z):

        print("yes")

    else:

        print("no")
