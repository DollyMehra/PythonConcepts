# a = int(input("enter any value between 5 and 9:"))

# if a < 5 or a > 9 :
#     raise ValueError("Value should be between 5 and 9")

a = input("Enter the word:")
if a.lower() != "quit":
    raise TypeError("Wrong desried input")
