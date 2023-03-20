# def addition(a,b):
   
#     sum  = a + b
#     print("this is sum of two numbers" , sum)

# a = 5
# b = 3

# addition(a,b)  



# def test():
#     pass

# def average(a=2,b=5):
#     print("the result is :" , (a+b)/2)

# average(a=5 ,b=15)   



def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is :",sum/len(numbers))  
    return sum /len(numbers)   

c=average(2,2,2)    
print(c)


