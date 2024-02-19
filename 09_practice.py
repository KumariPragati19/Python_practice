#make a function to find largest number
def greatest_number(num):
    largest_num=num[0]
    for i in range(0,len(num)-1):
        if num[i]<num[i+1]:
            largest_num=num[i+1] 
            i=i+1
    return largest_num
num=[1,2,36,8]
print(greatest_number(num))

#make a function to find largest in three number
def greatest_of_three(num1,num2,num3):
    if num1>num2 :
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3
print(greatest_of_three(8,9,4))

#or,
def greatest_of_three(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    if num2>num1 and num2>num3:
        return num2
    else:
        return num3
print(greatest_of_three(8,9,4))

#Write a function to convert far into celcius:
def farh(cel):
    return (cel*(9/5))+32
print("fahreheit temp is ",farh(7))

#how to prevent python print function in new line
print("hello",end=" ")
print("how",end=" ")
print("are",end=" ")
print("you",end=" ")
print("pragati")

#write a recursive function to calculate the sum of first n natural number
def sum_of_natural_no(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural_no(n-1)
print(sum_of_natural_no(10))

'''Write a function to print pattern
***
**
*
'''
def pattern(n):
    for n in reversed(range(1,n+1)):
        print(n*"*")
pattern(3)

#or,
m=5
for i in range(m):
    print("*"*(m-i))

#Write a python function to convert inches to cms
def inches_to_cm(number):
    return number*2.54
print(inches_to_cm(8))

#print strip of a string strip is that that it will print only written parnt not space.
this='     my name is pragati     '
print(this)
print(this.strip())
#now make a function to replace and strip the sentence
def String_Strip(sen,word):
    newStr=sen.replace(word,'')
    return newStr.strip()
sen=input()
word=input()
print(String_Strip(sen,word))

#Write a python function to print multiplication table of a given number
def multiplication(given_num):
    for i in range(1,11):
        mul_num=given_num*i
        print(mul_num)
given_num=int(input("Enter the number of multiplication you want : "))
multiplication(given_num)