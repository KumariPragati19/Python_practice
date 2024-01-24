'''If else and elif statements are a multiway decision taken by our
program  due to certain conditions in our code'''

#if-elif-else ladder
a=45
if (a>3):
    print('The value is greater than 3')
elif(a>7):
    print('The value is greater than 7')
else:
    print('the value is not greater than 3 or 7')
print('done')

#multiple if statements
#here we use assignment operators
if (a>3):
    print('The value is greater than 3')
if(a>7):
    print('The value is greater than 7')
else:
    print('the value is not greater than 3 or 7')
print('done')

# check age is greater than 18 which is given by user
age=int(input('Enter the age:\n'))
if age>18:
    print('Age is greater than 18.')
else:
    print('not greater')

# else is optional condition doesn't met any if condition and else is not give then it doesn't return anything