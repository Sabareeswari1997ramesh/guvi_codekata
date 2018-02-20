x=int(raw_input("Enter the Number:"))
if((0<x<1000000)|(-1000000<x<1)):
    if(x>0):
        print("Positive")
    elif(x<0):
        print("Negative")
    else:
        print("Zero")
else:
    print("enter valid input")