import re

def main():
    print(count(input("Text: ")))


def count(s):

    match =re.findall(r'\b(um)\b',s.lower())
    return len(match)

if __name__ == "__main__":
    main()