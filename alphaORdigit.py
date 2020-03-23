str = input("Enter the string:")
alpha = digits = 0

for i in range(len(str)):
    if((str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z')):
        alpha += 1
    elif(str[i] >= '0' and str[i] <= '9'):
        digits += 1

print("\nTotal number of Alphabets in this string are:", alpha)
print("\nTotal number of Digits in this string are:", digits)