
L={}
try:
    while True:
        element=input().upper()
        if element in L :
            L[element]+=1
        else :
            L[element]=1
except EOFError :
    L=dict(sorted(L.items()))
    for e in L:
        print(L[e],e)




