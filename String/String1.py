str=input("Enter a string: ")
upper=0
lower=0
for i in range(len(str)):
      if(str[i]>='a' and str[i]<='z'):
          lower+=1
      elif(str[i]>='A' and str[i]<='Z'):
          upper+=1
print('Lower case letters= ',lower)
print('Upper case letters=' ,upper)
