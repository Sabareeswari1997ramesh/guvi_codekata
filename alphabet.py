x=raw_input()

y=x.lower()

if y in('aeiou'):

    print("vowel")

elif y in('bcdfghjklmnpqrstvwxyz'):

    print("consonant")

else:

    print("Enter the valid input")