#wapp to do string copy opreation using user defined function
def copy(str1):
    str2 = ''
    for i in str1:
        str2 = str2 + i

    print("The String coped to Str2 is: ", str2)

str = input("Enter your string: ")
copy(str)