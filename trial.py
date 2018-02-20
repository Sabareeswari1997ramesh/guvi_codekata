x=int(raw_input("Enter the Number:"))
if(-1000001<x<1000001):
    if(x>0):
        print("Positive")
    elif(x<0):
        print("Negative")
    else:
        print("Zero")
else:
    print("enter valid input")