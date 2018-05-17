char=raw_input()

y=char.lower()

if y in('abcdefghijklmnopqrstuvwxyz'):

    print("Alphabet")

else:

    try:

        x=int(y)

    except ValueError:

        print("Enter the number or char only")

    else:

        print("No")
    
    