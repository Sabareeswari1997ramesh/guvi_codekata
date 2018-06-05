list=[]

n=int(raw_input())

k=int(raw_input())

for i in range(0,n):

    no=int(raw_input())

    list.append(no)

sum=0

i=0

while(i<k):

   sum=sum+list[i]

   i=i+1

print(sum)