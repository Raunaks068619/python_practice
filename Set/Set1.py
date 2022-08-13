num_set = set([2, 4, 0, 8, 5])
print("Original set:")
print(num_set)

def removeEle(n):
    num_set.remove(n)
    print("After removing {}:".format(n))
    print(num_set)

removeEle(8)    
