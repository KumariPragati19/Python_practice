a={2,8,9,5,2} #it is colecttion on non repetative elements
print(a)
print(type(a))

b={} #this will create empty dic not set
print(type(b)) #varify above line

c=set() #this is way we create empty set
print(type(c))

c.add(6)
c.add(9)
c.add(9)#it will not add this 9 because it add non repetative element
# c.add([9,8,6])   #beacuse list is not hasable that wise we cannot add list
# c.add({4:5})  #beacuse dict is not hasable that wise we cannot add dict
c.add((3,4,7)) #we can add tuples
print(c)

print(len(c)) #print the length of set

c.remove(6) #remove the value present in set
# c.remove(15) #throws error which is not presentr in set
print(c)

print(c.pop()) #remove any an arbitary element

c.clear() #empites the set
print(c)

d= {8,9,5,7}
print(d.union({22,88})) # add union means all value

print(d.intersection({6,8,22,4,1})) #return only common value


