s = int(input("Enter a string: "))
rev = 0
tempS = s

while(s > 0):
    rem = s % 10
    rev = (rev*10)+rem
    s = s//10

if(tempS == rev):
    print("%d is a palindrome number" % tempS)
else:
    print("%d is not a palindrome number" % tempS)
