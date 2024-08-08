
def main():
    z=check_main()
    if z<2:
        print('E')
    elif z>98:
        print('F')
    else :
        print(f'{z}%')


def check_main():
    while 1:
        fraction=input('Fraction : ')
        try :
            fraction=fraction.split('/')
            x=int(fraction[0])
            y=int(fraction[1])
            if y>=x and y!=0:
                z=round(x*100/y)
            else:
                continue
        except ValueError : pass
        else:
            break
    return z




main()





