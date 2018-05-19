try:

    x=int(raw_input())

except ValueError:

    print("Enter the integer only")

else:
    if(x<=1000):
        y=str(x)
        z=y[::-1]

        if(y==z):

            print("yes")

        else:

            print("no")
    else:
        print("enter the no within the limit")