                    #CALCULATE FACTORIAL USING A FUNCTION

#--------------------------------------------------------------------------#
#                            Using a while loop                            #
# -------------------------------------------------------------------------#
def factorial(n):
    total = 1
    while(n != 0):
        total = total * n
        n -= 1
    return total

n = int(input("Enter a number: "))
result = factorial(n)
print("Factorial of", n, "is:",result)

#--------------------------------------------------------------------------#
#                            Using Recursion                               #
# -------------------------------------------------------------------------#

def factorial(n):
    if (n < 2):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
result = factorial(n)
print("Factorial of", n, "is:",result)
