import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    ip_pattern= (r'^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.'
                r'([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.'
                r'([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.'
                r'([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$')
    if match:=re.search(ip_pattern,ip):
        return True
    else : return False


if __name__ == "__main__":
    main()
