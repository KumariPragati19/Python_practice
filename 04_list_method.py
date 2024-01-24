from re import L


l1=[1,8,3,0,5,3,8,6,1]
print(l1)
count=l1.count(1)#count the no of occurance of 1
print(count)
l1.sort() #sort the list
print(l1)
l1.reverse() #reverse the list
print(l1)
l1.append(60) #adds at the end of the list
l1.append(30)
print(l1)
l1.insert(3,45)  #insert the element
print(l1)
l1.pop(6) # remove element at index 6
print(l1)
l1 = list(filter((8).__ne__, l1))
l1.remove(1) #remove 1 from the list at oly once if multiple 1 present in it
l1 = list(filter((8).__ne__, l1)) #remove all 8 element present in list "using filter"
print(l1)
