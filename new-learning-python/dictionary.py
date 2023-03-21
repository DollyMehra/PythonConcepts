info = {
       "name": "dolly",
        "age" : 22 ,
        "eligible" : True
}


'''
print(info)
#if key is not present in dictionary then it will give error
print(info['name2'])

#if key is not preseent in dictonary then it will give NONE value
print(info.get('name2'))
'''


'''
print(info)
#output: {'name': 'dolly', 'age': 22, 'eligible': True}
print(info.items())
#output: dict_items([('name', 'dolly'), ('age', 22), ('eligible', True)])
'''

# print(info.keys())
# print(info.values())


########
'''
a = "dolly"
for key in info.keys():
    print(f"The value corresponding to the {key} is {info[key]}")

    """
   #for testing purpose I have tested this logic(for KBC game)
    if a == info[key]:
        print("hurrhh")
    """

 ######33   

 '''

 #another method to do this.

# for key , value in info.items():
#    print(f"the value corresponding to the {key} is {value}")
    
  #employeeID: their performance from 100  
ep1 = {101:10,102:40,103:60,104:95,105:58}
ep2 = {201:30,202:40}

ep1.update(ep2)
print(ep1)