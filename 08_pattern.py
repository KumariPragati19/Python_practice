'''print pattern
*
**
***
this. '''

for i in range(1,4):
    print("*"*i)

'''print pattern
  *
 ***
*****
this. '''

n=3
for i in range(1,n+1):
    print(' '*(n-i)+"*"*(2*i-1))

# or,

for i in range(3):
    print(' '*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(' '*(n-i-1))

'''print pattern
***
* *
***
this. '''

for i in range(1,4):
    if(i%2==0):
        print("*"+" "*(n-2)+"*")
    else:
        print("*"*n)

