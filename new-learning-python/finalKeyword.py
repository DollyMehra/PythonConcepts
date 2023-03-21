def func1():
 try:
   l = [1,5,6,7]
   i = int(input("enter the index:"))
   print(l[i])
 except:
   print("some error occured")  
 finally:
   print("i am always executed")  

x = func1()  
print(x)
#as we know that 'finally' keyword is always 
#executed either the program executed successfully or not 
#important question: why we use final keyword even we can use a print function .?
# answer: yes print function will also execeute but the main thing is if we use final keyword within the function the we can easily refer to the exact requirment..

