Song = 'Adieu, adieu, to'
L=[]
try :
    while True :
        name=input('Name: ')
        L.append(name)
except EOFError:
    if len(L)==1:
        print (Song,L[0])
    elif len(L)==2:
        print(f'{Song} {L[0]} and {L[1]}')
    else:
        L[-1]='and '+L[-1]
        for name in L :
            Song+=f' {name}'+','
        Song=Song[:-1]
        print(Song)
