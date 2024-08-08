text=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
text=text.replace(' ','').lower()
if text in ['42', "forty-two", "fortytwo"]:
    print('yes')
else : print('no')
