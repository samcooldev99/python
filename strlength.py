#wapp to find string length using user defined function
def length(str):
    count = 0
    for s in str:
        count = count + 1

    print("The length of the string is: ", count)

str = input("Enter the string:")
length(str)