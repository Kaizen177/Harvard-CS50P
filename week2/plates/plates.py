from re import search


def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if len(plate)>6:
        return False

    else:
        pattern="^[a-z]{2}[a-z]*([1-9][0-9]*)?$"
        if search(pattern,plate.lower()):
            return True
        else: return False

main()
