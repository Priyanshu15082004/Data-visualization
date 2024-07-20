firstlist=[20,30,40,50,60,30,60,50,34,80,45,65]
print("List is ")
print(firstlist)
#removefrom specified position 
firstlist.pop()
print( firstlist)
#to remove an element
firstlist.remove(50)
print(firstlist)
#to clear all element
firstlist.clear()
print(firstlist)
# deleting element in given range 
del firstlist[3:8:5]
print(firstlist)