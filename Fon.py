# wapp to display format number f(n)= (2^(2n))+1.
import math
n= int(input("Enter the value of 'n':"))
res = ((2^(2*n))+1)
#format display
if (n>0):
    print("The value of f(%d)=(2^(2*(%d))+1 is: %d" %(n,n,res))
else:
    print("The value should a non negetive interger")
