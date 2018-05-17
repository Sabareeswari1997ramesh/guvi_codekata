try:

    n=int(raw_input())

except ValueError:

    print("Enter only year in 4 digit integer format")

else:

    if(n%4==0):

        print("yes")

    else:

        print("no")