try:

    n=int(raw_input())

except ValueError:

    print("Enter only integer")

else:

    sum=0

    i=n

    while(i>0):

        sum=sum+i

        i=i-1

    print(sum)    
