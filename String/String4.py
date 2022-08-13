def removeX(n):
    for i in range(len(n)):
        if(n.endswith('x')):
            n = n[:-1]
        if(n.startswith('x')):
            n = n[1:]
    return n


str = input("Enter a string with x: ")
removeX(str)
