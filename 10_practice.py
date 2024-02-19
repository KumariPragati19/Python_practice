#Write a program to read the text from a given file 'poem.txt' and find out eeather it contains the words 'twinkle'
# f= open('poem.txt','w')
# f.write('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')
# f.close()

with open('poem.txt','r') as f:
    a=f.read()
f.close()