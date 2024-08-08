
text=input('camelCase : ')
for l in text :
    if l==text[0]: continue
    elif l.isupper():
        text=text[:text.index(l)]+'_'+l.lower()+text[text.index(l)+1:]
print(text)





