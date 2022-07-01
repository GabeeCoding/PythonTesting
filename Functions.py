v = 1
y = 0
def func(): # basic function which prints when called
    print("Works")

func() #call the function

def vartest():
    # global and local variables
    # if you set a variable in a function with the same name as a global variable
    # it is overidden in the fuction
    v = 2
    print(v) # 2
    # if you want to set a global variable in a function
    # use the global keyword
    global y
    y = 1
    print(y) # 1

vartest()
print(v) # v is 1 and not 2 because it was set locally in the function
print(y) # y is still 1 because of the global keyword

print("-------------------")

# Functions with arguments

def x20(number): # paramaters are in the brackets seperated by commas
    # paramaters are inputted when the function is called
    # 
    return number * 20

print(x20(0), x20(2), x20(500))