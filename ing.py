#function to add the ing at the end
def add_string(str):
    length = len(str)
    if length > 2:  
        if str[-3:] == 'ing':  
            print("The given string already contains the 'ing'")  
        else:  
            str += 'ing'
            print("The string is:"+str)

string = input("Enter the string:")
add_string(string)