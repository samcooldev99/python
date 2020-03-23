#pp to concatenate strings using user defined functions
#def concatenate(str1,str2):
#    while(str1[i]!='\0'):
#        ++i
#        while(str2[j]!='\0'):
#            ++j
#            ++i
#    str1[i]='\0'
#    print("Output: ", str1)

def concatenate(str1,str2):
    if str1 is None or str2 is None:
        print("Strings cannot be concatenated!!!")
    else:
        print("String on concatination:",str1 +" "+ str2)

str3 = input("Enter string one: ")
str4 = input("Enter string two: ")
concatenate(str3,str4)