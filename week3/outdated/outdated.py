import re

L={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

pattern1 = r'^(January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}), (\d{4})$'
pattern2 = r'^(\d{1,2})/(\d{1,2})/(\d{4})$'

def main():

    i=0
    while i==0:
        date=input('Date: ').strip()
        if check1(date)==1:
            date=convert1(date)
            if date!=5:
                i=1
                return '-'.join(date)
            else: pass


        elif check1(date)==2:
            date=convert2(date)
            if date!=5:
                i=1
                return '-'.join(date)
            else: pass

def check1(date):

    if re.match(pattern1,date):
        return 1
    elif re.match(pattern2,date):
        return 2

def convert1(date):

    date=date.split(' ')
    date[1]=date[1].replace(',','')
    date=[date[2],str(L[date[0]]),date[1]]
    if int(date[1])<13 and int(date[2])<31:
        date[1]='{:02d}'.format(int(date[1]))
        date[2]='{:02d}'.format(int(date[2]))
        return date
    else : return 5


def convert2(date):
    date=date.split('/')
    date=[date[2],date[0],date[1]]
    if int(date[1])<13 and int(date[2])<31:
        date[1]='{:02d}'.format(int(date[1]))
        date[2]='{:02d}'.format(int(date[2]))
        return date
    else : return 5




print(main())
