def lastDigit(num1, num2):
    if num1 % 10 == num2 % 10:
        return True
    else:
        return False


print(lastDigit(7, 17))
print(lastDigit(6, 17))
print(lastDigit(3, 113))
