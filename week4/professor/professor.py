import random


def main():

    score=0
    n=get_level()

    for _ in range(10):

        x,y=generate_integer(n)

        for i in range(3):

            a=input(f'{x} + {y} = ')
            try :
                int(a)
            except: print('EEE')
            else:
                if int(a)==x+y:
                    score+=1
                    break
                elif i<2 :
                    print('EEE')



        if i==2 and a!=x+y : print(f'{x} + {y} = {x+y}')

    print(f'Score: {score}')







def get_level():

    while True :
        n=input('Level: ')
        try :
            int(n)
        except : pass
        else :
            if int(n) in [1,2,3]: return int(n)


def generate_integer(level):
    l=level
    if l==1:
        x=random.randint(0,9)
        y=random.randint(0,9)
        return x,y
    elif l==2:
        x=random.randint(10,99)
        y=random.randint(10,99)
        return x,y
    elif l==3:
        x=random.randint(100,999)
        y=random.randint(100,999)
        return x,y


if __name__ == "__main__":
    main()
