#wapp to compare string using user defined function
def comp(str1,str2):
    if str1 == str2:
        print("Strings are matching")
    else:
        print("Strings do not match")

str = input("Enter the string 1: ")
str0 = input("Enter the string 2: ")
comp(str,str0)