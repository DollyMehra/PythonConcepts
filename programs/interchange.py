# python program to interchange first and last number

#first method
"""
def swapList(newList):
    size = len(newList)

    #swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

newList = [1,2,3,4]
print(swapList(newList))

"""
#second method
def swapList(newList):
    newList[0] , newList[-1] = newList[-1] , newList[0]
    return newList

newList = [1,2,3,5]
print(swapList(newList))


