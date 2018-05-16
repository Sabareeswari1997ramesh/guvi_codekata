y=raw_input()

x=y.lower()

if((x=='monday')|(x=='tuesday')|(x=='wednesday')|(x=='thursday')|(x=='friday')|(x=='saturday')|(x=='sunday')):

    if((x=='monday')|(x=='tuesday')|(x=='wednesday')|(x=='thursday')|(x=='friday')):

        print("no")

    else:

        print("yes")

else:

    print("Enter the valid input")