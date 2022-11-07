#1. Create a simple function that takes 2 numbers and print their values
'''
def mah ():
    x = 5
    y = 10
    print (x+y)
'''
#2. Create a simple function that takes 2 numbers and return their values
'''
def mah ():
    x = 5
    y = 10
    return (x+y)
'''
#3. In the above return function, use keyword arguments when calling the function
'''
mah ()
'''
#4. In the above return function, give x and y default values of 0 and call the function with no arguments
'''
def mah (x=0, y=0):
    result = x+y
    return (result)
l= mah ()
print (l)
'''
#5. Create a function that can take any number of arguments and print the sum of them
'''
def mah (x,y):
    result = x+y
    return(result)
l= mah (4,4)
print(l)
'''
#6.Create the same sum function using the lambda
'''
mah22 = lambda x,y : x+y
'''
#7. Call the lambda function at the same definition line
'''
(lambda x,y : x+y)(4,4)
'''

#8. Write the difference between the local variable and global variable
'''
Local variables: can only be accessed within the function or module in which they are defined,
global variables: can be used throughout the entire program
'''








