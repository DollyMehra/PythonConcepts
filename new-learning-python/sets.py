'''
#to create a empty set
#in dictionary also it start with curly braces and end with curly braces just like sets.
#so to know the type of set we have to do like this dolly = set()
dolly = set()
print(type(dolly))


#there is no order of set 
# and we cant get the repititive values in set
items = { "apple" , 0.1 , True , 88 , 88 , 9 , -9}
for i in items:
    print(i)

''' 

'''
s1 = {1,2, 3, 4 ,5}
s2 = {5, 6, 7}
print(s1,s2)
print(s1.union(s2))
print(s1.intersection(s2))
#it will remove the comman values
print(s1.symmetric_difference(s2))
print(s1.update(s2))
print(s1,s2)
#pop element will pop random element
print(s1.pop())
print(s1)
'''

'''

cities = {"delhi", "mumbai" , "punjab"}
# cities.remove("delhi")
# print(cities)

#if we use 'remove' and element is not present in set then it will give error.
#sometimes it is useful in programs to get errors for troubleshooting
# cities.remove("delhi111")
# print(cities)

#if we dont want to get an error then we can use a 'discard' as well

cities.discard("delhi111")
print(cities)

'''

#'clear' method clears the entire items from set 
#'del' method delete the entire set



