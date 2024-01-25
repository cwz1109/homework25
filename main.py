# Homework 3


while True:
    A = {0}

    a = str(input())
    A.update(a)

    if a == "end":
        break
print(A)

# How to ask for the sets ?

quit()
# Homework 2 List
#Write Python code that asks the user for a list of numbers (floats) one by one and stops
#once the user doesn’t enter a valid number. Once the numbers are in the list the program should calculate the mean average. For example, if they enter:
# 1  2 3
# Bla bla bla I’m finished. It calculates a mean average of 2.0

mylist = []
while True:
    x = (input("Give me some integers:"))
    mylist.append(x)
    X = len(mylist)

    try:
        c = float(x)

    except:
        break


N = []
for item in mylist:
    if item == float:
        N.append(item)

print(X-1)
print(sum(N)/X)

# How to calculate them ?


quit()
# Homework 1 Error
# Check that x is an int and raises an error if it is not (Type Error)
# Check that x is positive and raises an error if it is not (Value Error)
# Assert that x must be less than 20
# Returns the root of the factorial of x

x = (input("x = "))
try:
    z = int(x) # replace x to z
except ValueError:
    raise TypeError("TypeError, this is not an int.")
# make a personal Type error
if z > 0:
    print()

else:
    raise ValueError("ValueError, this is not positive.") # make a value error

# define a function
def rootfactorial(z):
    if z==1 :
        y=z
        return y

    else:
        y=z*rootfactorial(z-1)
        return y
# return the root
print("Return:", rootfactorial(z))

# About "Assert that x must be less than 20"
# How to do it ?

