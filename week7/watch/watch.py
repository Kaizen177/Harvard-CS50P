import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern=r'^<iframe.* src="https?://(?:www\.)?youtube\.com/embed/([^"]+)".*></iframe>$'
    if url := re.search(pattern,s.strip()):
        yid= 'https://youtu.be/'+url.group(1)
        return yid
    else:
        return None


if __name__ == "__main__":
    main()
