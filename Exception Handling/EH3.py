try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
    print("a/b = %d"%c)    
except Exception as e:    
    print("can't divide by zero")    
    print(e)  
else:    
    print("Hi I am else block")  
