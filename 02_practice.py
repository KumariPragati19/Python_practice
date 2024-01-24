name=input()
print("good afternoon, "+ name)
date=input()
letter='''Dera<|Name|> ,
your are selected!
Date:<|Date|>'''
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)
letter1= "Dear, today's weather is nice. Thanks!"
formatted_letter1="Dear,\n \t today's weather is nice. \nThanks!"
print(formatted_letter1)