#use open function to read the content of a file!
f=open('sample.txt','r') #if we not select the mode it take by default read
data=f.read()
data1=f.read(5)#read till 5 character we need to create another becase if we read file once then we cannot read again
print(data)
print(data1)
f.close()