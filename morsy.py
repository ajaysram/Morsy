#! /usr/bn/env python3
morse= {
    'A':'._',
    'B':'_...',
    'C':'_._.',
    'D':'_..',
    'E':'.',
    'F':'.._.',
    'G':'__.',
    'H':'....',
    'I':'..',
    'J':'.___',
    'K':'_._',
    'L':'._..',
    'M':'__',
    'N':'_.',
    'O':'___',
    'P':'.__.',
    'Q':'__._',
    'R':'._.',
    'S':'...',
    'T':'_',
    'U':'.._',
    'V':'..._',
    'W':'.__',
    'X':'_.._',
    'Y':'_.__',
    'Z':'__..',
    '.':'._._._',
    ',':'__..__',
    '?':'..__..',
    '/':'_.._.',
    '@':'.__._.',
    '1':'.____',
    '2':'..___',
    '3':'...__',
    '4':'...._',
    '5':'.....',
    '6':'_....',
    '7':'__...',
    '8':'___..',
    '9':'____.',
    '0':'_____',

}

code = []
text = input("Enter the message :")
newForm = text.upper()
msg = list(newForm)
for letter in msg:
    for alphabet in morse.keys():
        if alphabet == letter:
            code.append(morse[alphabet])
code = ''.join(str(element) for element in code)
print("Morse Coded value :",code)