import validator_collection


def main():

    e = input("What's your email address? ")
    try:
        validator_collection.email(e)
    except :
        print('Invalid')
    else : print('Valid')



if __name__ == "__main__":
    main()


