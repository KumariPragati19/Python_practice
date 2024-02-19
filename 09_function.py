#we create function for reuse it again and again and it has return statements

def percentage(marks):
    p= (sum(marks)/400)*100
    return p

marks1=[45,89,26,55]
percentage1=percentage(marks1)

marks2=[45,89,90,49]
percentage2=percentage(marks2)
print(percentage1, percentage2)

#Function to greet 

def greet(name="chi chi"):
    print ("Hello "+name)

greet("Pragati")
greet() #default value store in name as chi chi will print here bcz we sotre chi chi as default as default value
name= input("Enter your name: ")
greet1=greet(name)

#Sum operation function
def mySum(num1,num2):
    return num1+num2
sum=mySum(9,4)
print(sum)

#print factorial of a number
def factorial_iter(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
print(factorial_iter(7))

def factorial_recursive(m):
    if m==1 or m==0:
        return 1
    else:
        return m *factorial_recursive(m-1)
print(factorial_recursive(7))