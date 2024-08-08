
def main():

    text=input('hello : ').lower()
    print(value(text))


def value(text):

    if 'hello' == text[:5]:
        return 0
    elif 'h'==text[0]:
        return 20
    else :
        return 100



if __name__ == "__main__":
    main()
