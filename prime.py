n = int(input("Enter the value of 'n': "))  
m = int(input("Enter the value of 'm': "))  
  
for num in range(n,m + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  