x=int(raw_input())

if((x>=0)&(x<10000)):

    if(x<1000):

        i=x/100

        j=x%100

        k=j/10

        l=j%10

        print(str(l)+str(k)+str(i))

    elif(x>1000):

        u=x/1000

        v=x%1000

        w=v/100

        y=v%100

        p=y/10

        z=y%10

        print(str(z)+str(p)+str(w)+str(u))

else:

    print("Enter the valid input")