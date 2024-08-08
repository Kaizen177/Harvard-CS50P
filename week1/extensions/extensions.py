
#Extensions data

l1=['gif','jpg','jpeg','png','pdf','txt','zip']
l2=['image/gif','image/jpeg','image/jpeg','image/png','application/pdf','text/plain','application/zip']

#Main Program

def main():
    text=input('File name = ').lower().replace(' ','').split('.')
    ext=text[-1]
    if ext in l1:
        i=l1.index(ext)
        print(l2[i])
    else : print('application/octet-stream')
main()
