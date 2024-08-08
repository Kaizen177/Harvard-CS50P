

def main ():
    print('Amount Due: 50')
    d=0
    while 50-d>0 :
        c=int(input('Insert Coin: '))
        if c in [5,10,25]:
            d+=c
            if 50-d>0 : print(f'Amount Due: {50-d}')
            else : print(f'Change Owed: {d-50}')
        else :
            print(f'Amount Due: {50-d}')


main ()




