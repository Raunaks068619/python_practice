lst=[1,2,3,4,5,-6,-7,-8,9,-10]
index=int(input("Enter an index : "))

try:
    if lst[index] > 0:
        print ("Positive")
    else:
        print ("Negative")
except:
    print ("Index out of range")
