'''
a = input("Enter the number")
print(f'Multiplication table of {a} is:')

try:
   for i in range(1,11):
      print(f'{int(a)} X {i} = {int(a) * i}')
#except Exception as e:
   #print(e) 
#we can also use only except here . It will not halt the program
except:   
     print("Invalid input")     
print("Some important lines of code ")

'''

'''
try:
    num = int(input("Enter an integer"))
except ValueError :
    print("number entered is not integer")  

'''


try:
    num = int(input("Enter an integer: " ))
    a = [6,3]
    print(a[num])
except IndexError:
    print("index error")
except ValueError:
    print("number enterded is not an integer")    

#help link: https://www.programiz.com/python-programming/exceptions     

 