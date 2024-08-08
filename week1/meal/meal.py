def main():
    t=convert(input('What time is it : '))
    if 7<=t<=8: print('breakfast time')
    elif 12<=t<=13: print('lunch time')
    elif 18<=t<=19: print('dinner time')

def convert(time):
    t=checkm(time)
    x,y=int(t[0]),float(t[1])
    y=round(y/60,2)
    return x+y

def checkm(t):
    if t[-4:]=='a.m.':
        t=t[:-5]
        return t.split(':')
    elif t[-4:]=='p.m.':
        t=t[:-5].split(':')
        x,y=str(int(t[0])+12),t[1]
        return [x,y]
    else : return t.split(':')

if __name__ == "__main__":
    main()
