import random


while True:
    n=input('Level: ')

    if n.isdigit() and int(n)>0:
        break
    else : continue

a=random.randint(1,int(n))

while True:
    b=input('Guess :')
    if b.isdigit() and int(b)>0:
        b=int(b)
        if b>int(n):
            print('Too large!')
        elif a==b :
            print('Just right!')
            break
        elif a>b :
            print('Too small!')
        elif a<b:
            print('Too large!')

    else:continue



