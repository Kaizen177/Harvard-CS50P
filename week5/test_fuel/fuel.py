


def main():
    fraction=input('Fraction: ')
    print(gauge(convert(fraction)))

def convert(fraction):

    fraction=fraction.split('/')
    x,y=fraction[0],fraction[1]

    if int(y)==0:
        raise ZeroDivisionError
    elif (not (x.isdigit() and y.isdigit())) or int(x)>int(y):
        raise ValueError
    else:
        x=int(x)
        y=int(y)
        z=round(x*100/y)
        return z


def gauge(percentage):
    z=percentage
    if z<2:
        return'E'
    elif z>98:
        return 'F'
    else :
        return f'{z}%'


if __name__ == "__main__":
    main()









