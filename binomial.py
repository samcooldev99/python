# A naive recursive Python implementation 
  
def binomialCoeff(n , k): 
  
    if k==0 or k ==n : 
        return 1
  
    # Recursive Call 
    return binomialCoeff(n-1 , k-1) + binomialCoeff(n-1 , k) 
  
# Driver Program to test ht above function 
n = int(input("Enter the value of 'n':"));
k = int(input("Enter the value of 'k':"));

print ("Value of C(%d,%d) is (%d)" %(n , k , binomialCoeff(n , k)))
