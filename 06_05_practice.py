#print the meaning of words given by user
dict_hidi_words = {
    'nak':'nose',
    'pankha':'fan',
    'kamal':'lotus',
    'suraj':'sun',
    'kalam':'pen'
}
print('options are: ',dict_hidi_words.keys())
a=input('Enter the word to transalte in english: ')
print('the meaning of your word is: ',dict_hidi_words.get(a))

#print only unique value given by user
c=set()
for i in range(1,9):
    num=int(input(f'Enter the number{i}:\n'))
    c.add(num)
print(c)

#find if we store 18 as int and 18 as str then what it will print
s={18,'18',18.1}
print(s)

#length of this set s1
s1={18,'18',18.0} #18.0,18 considered as same
print(len(s))

#allow friend to enter their fav languague and you can acess that
fav_lang={}
for i in range(0,5):
    name=input("Enter your name:\n")
    lang=input("Enter your fav lang:\n")
    fav_lang[name]=lang
print(fav_lang)