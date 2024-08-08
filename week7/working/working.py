import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    regex= "(0?[0-9]|1[012]):?([0-5][0-9])? (am|pm)"
    pattern= r"^" + regex + " to " + regex + "$"


    if time:= re.fullmatch(pattern,s.strip().lower()):

        time=list(time.groups())
        for i in [0,1,3,4]:

            if time[i]==None:
                time[i]=0
            else: time[i]=int(time[i])

        for i in [2,5]:
            if time[i]=='am' and time[i-2]==12:
                time[i-2]=0
            elif time[i]=='pm'and time[i-2]!=12:
                time[i-2]+=12
        ntime = f'{time[0]:02}:{time[1]:02} to {time[3]:02}:{time[4]:02}'
        return ntime

    else: raise ValueError


if __name__ == "__main__":
    main()


