#1.  print gretest number

# first method
a=[]
for i in range(1,5):
    num = int(input(f'Enter the number {i}: '))
    a.append(num)
a.sort()
print(a[3])

#second method
num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))
num4= int(input("Enter number 4: "))
if num1>num4:
    f1=num1
else:
    f1=num2

if num2>num3:
    f2=num2
else:
    f2=num3

if f1>f2:
    print(f1 , " is greatest.")
else:
    print(str(f2) + " is greatest.")

# -----------------------------------------------------------------------------------------

#2. PASS OR FAIL SUBJECT WISE
sub1=int(input("Enter first subject marks: "))
sub2=int(input("Enter second subject marks: "))
sub3=int(input("Enter third subject marks: "))
total= (sub1+sub2+sub3)/3
if(sub1<33 or sub2<33 or sub3<33):
    print('You fail')
if(total>40):
    print('You pass')
else:
    print('you fail')
    

# -----------------------------------------------------------------------------------------------------------------------------------

#3. DETECT SPAM MESSAGE
#first approach
msg=input("")
if(msg=='make a lot of money' or msg=='buy now' or msg=='buy now' or msg=='subscribe this' or msg=='click this'):
    print('this is spam msg')
else:
    print(msg)

#little advance approch
msg=input("")
if('make a lot of money' or 'buy now' or 'subscribe this' or 'click this' in msg):
    print('this is spam msg')
else:
    print(msg)


# --------------------------------------------------------------------------------------------------------

#4. WEATHER A GIVEN USERNAME CONTAINS LESS THAN 10 CHARACTER OR NOT
name=input("Please enter your name: ")
if(len(name)>=10):
    print("Length is greater than 10")
else:
    print("length is less than 10.")


# ----------------------------------------------------------------------------------------------------

#5. find weather the name present in list or not
name_list=['sita','raj','arun','raghu','neha','arti']
find_name=input('Enter the name: ')
if find_name in name_list:
    print("Your name present is the list.")
else:
    print("your name is not present in the list.")


# --------------------------------------------------------------------------------------------------------------------

#6.Print the grade according to marks
marks=int(input("Enter the marks: "))
if marks>=90:
    print('Ex')
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
else:
    print('F')

#---------------------------------------------------------------------------

#7.talking about harry or not case insensitive
comment=input("comment: ")
comment=comment.lower() #convert all the letters into lowercase
if 'harry' in comment:
    print("talking about Harry")
else:
    print('not about Harry')