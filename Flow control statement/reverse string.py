# x = input("Enter a number to reverse: ")
# list = []
# for i in x:
#     list.append(i)

# list.reverse()

# for i in list:
#     print(i, end="")

n=int(input("enter number:"))
reverse=0
while(n>0):
    reminder=n%10
    reverse=(reverse*10)+reminder
    n=n//10
print("\n reverse of entered number = %d"%reverse)