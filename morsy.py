#! /usr/bin/env python3
import subprocess
import time
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
    ' ':'\n',
    '|':'\n'

}

code = []
text = input("Enter the message :")
msg = text.upper()
msg = list(msg)
for letter in msg:
    for alphabet in morse.keys():
        if alphabet == letter:
            code.append(morse[alphabet])
viewCode = ''.join(str(element) for element in code)
code = list(viewCode)
print("\n\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n")
print("MESSAGE : ",text,"\n")
print("MORSE CODE CONVERSION :")
print(viewCode,"\n")
for element in code:
    if element == '.':
        subprocess.call(["aplay","./audio/dit.wav"],stderr=subprocess.DEVNULL)
    elif element == '_':
        subprocess.call(["aplay","./audio/dah.wav"],stderr=subprocess.DEVNULL)
    else:
        time.sleep(0.2)    