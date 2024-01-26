#1. Write a program to print multiplication table of agiven number using for loop
num= int(input("Enter the number whose multiplication you want to know: "))
for i in range(1,11):
    num1=i*num
    print(f"{num}x{i}={num1}")

#--------------------------------------------------------------------------------------------------------
#2. Write a program to great all the persons name store in list and which is start with S
l1=['sid','mahi','sona','arun','raghu']
for i in l1:
    name=i.lower()
    if(name[0]=='s'):   #or we can use name.startswith("s")
        print(f"good morning {i}")
else:
    print("done")

#--------------------------------------------------------------------------------------------------------

#3. Attempt 1 using while loop
i=1
while i<=10:
    print(i*num)
    i=i+1

# ------------------------------------------------------------------

#4.Write a program to print sum of natural number using while loop
n=int(input('enter  till the num you want to sum : '))
i=1
sumofn=0
while i<=n:
    sumofn=sumofn+i
    i=i+1
print(sumofn)

# or by simple math
m=int(input('enter  till the num you want to sum : '))
sumofn1=(m*(m+1))//2
print(sumofn1)

#--------------------------------------------------------------------------------------------

#5. Write a program to check given number is prime or not

number=int(input("Enter the num to check prime: "))

prime=True
for i in range(2,number):
    if number%i==0:
        prime=False
        break
if prime:
    print("prime")
else:
    print("not prime")

# ----------------------------------------------------------------------------------------------

#6.write a program to find factorial of number
fact=1
num_fact=int(input("Enter the num you want to know its factorial: "))
for i in range(1,num_fact+1):
    fact=i*fact
print(fact)

#or,
fact=1
i=1
while i<=num_fact:
    fact=i*fact
    i=i+1
print(fact)

#-----------------------------------------------------------------------
#7. Write a program to print multiplication table of n using for loop in reversed order

num=int(input("Enter the number: "))
for i in range(10,0,-1):
    i=num*i
    print(i)