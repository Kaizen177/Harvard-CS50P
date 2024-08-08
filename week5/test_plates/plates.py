
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if (2 <= len(s) <= 6)== False:
        return False
    else :
        for i in s :
            if not i.isalpha():
                a = s.index(i)
                s1,s2=s[:a],s[a:]
                break
        else: return True
        if s2[0]=='0':
            return False
        elif len(s1)<2:
            return False
        else:
            return (s1.isalpha() and s2.isdigit())



if __name__ == "__main__":
    main()
