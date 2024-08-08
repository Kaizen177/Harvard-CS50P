
def main():
    word=input('Input: ')
    print(shorten(word))



def shorten(word):
    v=['a','e','i','o','u']
    for l in word :
        if l.lower() in v :
            word=word.replace(l,'')
    return word


if __name__ == "__main__":
    main()
