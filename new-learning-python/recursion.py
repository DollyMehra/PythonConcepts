
'''
#
# 5! = 5 * 4 * 3 * 2 * 1
#print the factorial of number

n = int(input("Enter the number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
      return n * factorial(n-1)
    
print(factorial(n))    
'''

"""
#print a fibonacci series
# 0 1 1 2 3 5 8
# 0 1 2 3 4 5 6 

n = int(input("Enter the number: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n < 0:
        print("Incorrect Input")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(0))  
# print(fibonacci(1)) 
# print(fibonacci(4))
print(fibonacci(n))   
"""