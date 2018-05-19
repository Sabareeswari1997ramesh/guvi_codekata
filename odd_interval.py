try:

    x=int(raw_input())

    y=int(raw_input())

except ValueError:

    print("enter integer inputs only")
else:

    if(x<y):

        i=x+1

        while(i<y):

            if((i%2)!=0):

                print(i)

            i=i+1

    elif(x>y):

        i=y+1

        while(i<x):

            if((i%2)!=0):

        	    print(i)

            i=i+1

    else:

        print("Enter different integer inputs")
    
    