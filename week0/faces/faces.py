#Faces_code

def convert(text):
    return text.replace(':)','🙂').replace(':(','🙁')
def main():
    txt=input('input your text =  ')
    print(convert(txt))
main()

