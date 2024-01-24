#it is mutable and it is unordered cannot contain duplicate key if it happens the it will override the value
myDict={
    "fast":"in a quick manner",
    "name":"work",
    "marks":[1,3,5,7],
    "another_dict":{'harry':'player'},
    1:2
}
print(list(myDict.keys())) #print keys
print(list(myDict.values())) #print the values of keys
print(list(myDict.items()))  #return tuple and print keys and values in the form of list

myDict.update({"lovish":"Friend",'riya':'friend','name':'raj'}) #update the dictionary by adding the key-value pairs, cann't use in myDict.upadte(updatedDict)
print(myDict)

print(myDict.get("name2")) #print valu associated with key "name"
print(myDict["name2"])     #print valu associated with key "name"

#but the difference between both is that if key is not present in dict the what it will show
print(myDict.get("name2")) #it shows none as return value
print(myDict["name2"]) #but it throws an error as name is not present in the dictionary that is keyerror