a = [1, 3, 1, 2, 4, 1, 1, 5, 6, 5, 5]

print(a)
def occurance(n):
    item = n
    count = 0
    for i in range(0, len(a)-1):
        if(item == a[i]):
            count = count + 1
            if(count == 2):
                del a[i]
                break

occurance(1)
print(a)
