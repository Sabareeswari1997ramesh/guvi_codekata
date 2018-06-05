list=[]

n=int(raw_input())

if(1<=n<=100000):

    for i in range(0,n):

        no=int(raw_input())

        list.append(no)

    print(max(list))

else:

    print("enter no within the limit")
    
	