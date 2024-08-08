import sys
import pyfiglet
import random

L=pyfiglet.FigletFont.getFonts()

if len(sys.argv)==1:
    text = input('Input: ')

    a=random.choice(L)
    f = pyfiglet.figlet_format(text,font=a)
    print(f'Output: {f}')



elif len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font')and sys.argv[2].lower() in L :
    text = input('Input: ')
    f = pyfiglet.figlet_format(text,font=sys.argv[2].lower())
    print(f'Output: {f}')

else:
    sys.exit('Invalid usage')





