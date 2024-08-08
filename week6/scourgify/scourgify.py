
import csv
import sys



def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try: o=open(sys.argv[1])
        except FileNotFoundError:
            sys.exit(f'Could not read {sys.argv[1]}')
        else:
            with o as file:

                after=[['first', 'last', 'house']]
                lines=csv.reader(file)
                next(lines)
                for row in lines:
                    name=(row[0].replace(' ','')).split(',')
                    newrow=[name[1]]+[name[0]]+[row[1]]
                    after.append(newrow)

            with open(sys.argv[2],'w',newline='') as file:

                nlines=csv.writer(file)
                nlines.writerows(after)




if __name__ == "__main__":
    main()
