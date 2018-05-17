x=int(raw_input())

if((x>=0)&(x<=100000)):

    y=x%2

    if(y==0):

        print("Even")

    else:

        print("Odd")

else:

    print("Enter the valid input")