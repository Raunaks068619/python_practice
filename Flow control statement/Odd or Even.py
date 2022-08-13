def checkOddEven(num):
    if num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))


checkOddEven(int(input("Enter a number: ")))