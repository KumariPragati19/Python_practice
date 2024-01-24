l=[]
for i in range(1,8):
  user_input =input(f"Enter the {i} of seven fruits: \n")  
  l.append(user_input)
print(l)

marks=[]
for i in range(1,8):
  mark =int(input(f"Enter the {i} of student marks: \n"))  
  marks.append(mark)
marks.sort()
print(marks)


l1=[1,5,8,20]
print(sum(l1)) #one method
sum=0 #another method
for i in range(0,4):
  sum+=l1[i]
print(sum)


a=[0,9,0,0,0,8,0,6]
count=a.count(0)
print(count)

a=(0,9,0,0,0,8,0,6)
count=a.count(0)
print(count)