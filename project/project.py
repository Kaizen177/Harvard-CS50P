import sys

#Website Parsing modules
import requests
from bs4 import BeautifulSoup

#Highlighting modules
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import RtfFormatter



def main():

    '''
    main function Handles user input and generates RTF files for lecture notes.

    - Parses command-line arguments to select lectures and sections.
    - Retrieves lecture titles and creates RTF files based on input.
    - Exits with an error message for incorrect arguments input.

    '''

    L = get_lectures('https://cs50.harvard.edu/python/2022/')
    argSyntax = ('\nUsage : [1: all] or [1: LectureNumber 2: "section1-section2-section3" ...]'
                +'\nIf sections not provided, all lecture sections will be printed.')

    if len(sys.argv) not in [2,3]:
        sys.exit('No arguments provided.' + argSyntax if len(sys.argv) == 1 else 'Too many arguments.' + argSyntax)

    else :
        if sys.argv[1].lower()=='all':
            print('Second argument ignored, first argument = "all"')
            for i in range(len(L)): create_rtf(i, L[i])

        else :
            if not sys.argv[1].isdigit() or int(sys.argv[1]) not in range(len(L)): sys.exit('Incorrect first argument'+ argSyntax)
            elif len(sys.argv) == 2: create_rtf(int(sys.argv[1]), L[int(sys.argv[1])])
            else:
                Sections = [sec.replace('"','') for sec in sys.argv[2].split('-')]
                create_rtf(int(sys.argv[1]), L[int(sys.argv[1])], Sections)


### Parsing Functions ###


def get_lectures(link:str):

    #Append all the lecture titles to L
    soup = BeautifulSoup(requests.get(link).text,'html.parser')
    lectures = soup.find('ol').find_all('li')
    L=[e.text for e in lectures]
    return L

def get_sections_content(n:int,sections:list):

    '''
    get_sections_content function takes the number of the lecture, the sections wanted by the user
    (if sections == [] the function will then return all the section in the lecture);

    get_sections_content return 2 lists;
    sections_content : list of lists, each one of the sublists contain the content of a section as tuples
    sections_titles : another list that contain the section titles

    '''

    sections=[e.lower() for e in sections]
    sections_content, sections_titles = [], []

    # Get course link html script
    r=requests.get(f'https://cs50.harvard.edu/python/2022/notes/{str(n)}/')
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all the section headers
    s=soup.find_all('h2')
    s_ids = {e.text.lower():e.get('id') for e in s}
    sections_titles = [e for e in s_ids]

    # Check all the elements in sections are sections titles of the course
    if not all(elem in sections_titles for elem in sections ):
        sys.exit("Some sections provided do not match the course sections.")

    # if sections specified replace them with the course section titles
    if sections:
        sections_titles = [e for e in sections_titles if e in e in sections]

    # Add each section content to sections_content list
    for s in sections_titles:

        sec=[]
        h2 = soup.find('h2',id=s_ids[s]) # Find section header
        sec.append((h2.text,'stitle'))
        if h2.find_next().name == 'p':
            sec.append((h2.find_next().text,'p')) # Add the p element before ul if exist
        ul=h2.find_next('ul')
        sec += ul_to_tuples(ul) # Add ul element as tuples
        sec+=add_h3(ul) # Add sub-section content

        sections_content.append(sec) # Add the section content to the main list of section
    return sections_content,sections_titles

def ul_to_tuples(sec:BeautifulSoup):

    '''
    ul_to_tuples function transform a ul html element (<ul>...</ul>) into a list of tuples;
    The elements inside the ul element are assigned into a 2-tuple representing the
    content of the element and its type.  ('text','p')

    '''
    l=[]

    # Find all the li(s) inside the ul element
    for li in sec.find_all(['li']):

        ppre=li.find_all(['p','pre'])

        # if pre element found, add all its element inside into l
        if ppre :
            for elem in ppre :
                l.append((elem.text,elem.name))
        else:
            l.append((li.text,li.name))
    return l

def add_h3(ul:BeautifulSoup):

    '''
    Similary to the ul_to_tuples function, add_h3 check if there is sub-section,
    adds its content (if existing) to a list of tuples.

    '''
    r = []
    while True:
        h3 = ul.find_next_sibling()

        # Break the loop if no more siblings or no h3 tag found
        if h3 is None or h3.name != 'h3':
            break
        r.append((h3.text, 'sstitle'))

        # Find the ul following the h3 tag
        h3ul = h3.find_next('ul')
        h3sec = ul_to_tuples(h3.find_next('ul'))
        r.extend(h3sec)
        ul = h3ul
    return r


### Formating Functions ###


def create_rtf(n:int,ltitle:str,t=[]):

    '''
    create_rtf function adds the first and table page, then adds the lecture sections;
    Each section is added separately and each part of the section is formatted with its own
    format style.

    '''
    lrtf = f'CS50P-L{n}.rtf'# File name
    content,st = get_sections_content(n,t)
    add_first_page(n,ltitle)
    add_table_page(st,lrtf)
    for section in content:
        for tupl in section:
            if tupl[1] == 'stitle': add_section_title(tupl[0],lrtf)
            elif tupl[1] in ['p','li']: add_dot(tupl[0],lrtf)
            elif tupl[1] == 'pre': add_code(highlight_(tupl[0]),lrtf)
            elif tupl[1] == 'sstitle': add_sub_section_title(tupl[0],lrtf)
        if section in content[:-1] : new_page(lrtf) # Not adding new page for the last section
    close_rtf(lrtf)

def highlight_(code:str):

    formatter = RtfFormatter(full = True, style = 'rainbow_dash')
    highlighted_code = highlight(code, PythonLexer(), formatter)

    #Removing the style part
    index = highlighted_code.find(r'\dntblnsbdb')+len(r'\dntblnsbdb')
    return highlighted_code[index:].strip()[:-1]

def correct_(text:str):

    # Correct some rtf enconding errors
    ct = ''
    for l in text:
        if l in ['‘','’']:
            ct += "'"
        elif l in ['”','“']:
            ct += '"'
        elif l == '…':
            ct+='...'
        else : ct += l
    return ct

def add_first_page(n:str,ltitle:str):

    #Add first page content to the file
    with open('style.txt', encoding = 'utf-8') as f:
        style = f.read()
    ctitle = "CS50\'s Introduction to Programming with Python"
    lecture = f'Lecture {n} Notes'
    content = ( style + '\n'+ r'\par' * 8
               + '\n' + rf'{{\f1\b\cf7\fs72 {ctitle}}}\par' +'\n'+ r'\fs72\par'
               + '\n' + rf'{{\f1\b\cf17\fs72 {lecture}}}\par'
               + '\n' + rf'{{\f1\b\cf7\fs68 {ltitle}}}\par' +'\n'+ r'{\fs74\par}' * 5
               + '\n' + rf'{{\f1\fs32\cf17 David J. Malan}}\par'
               + '\n' + rf'{{\f1\fs32\cf17 Harvard University}}\par'
               + '\n' + rf'{{\f1\fs32\cf17 cs50.harvard.edu/python/2022}}\par\page')

    with open(f'CS50P-L{n}.rtf', 'w', encoding='utf-8') as file:
        file.write(content)

def add_table_page(st:list,mainrtf:str):

    #Add table content to the file
    st = [e.title() for e in st]
    content = '\n' + r'{\f1\b\cf7\fs64 Table :}\par'+ '\n'+ r'\fs48\par'

    with open(mainrtf, 'a', encoding='utf-8') as file:
        file.write(content)
    for e in st :
        add_dot(e,mainrtf)
    with open(mainrtf, 'a', encoding='utf-8') as file:
        file.write(r'\page')

def add_section_title(st:str,main_rtf:str):

    stitle = rf'{{\f1\b\ul\cf7\fs48 {st}\par}}'

    #Add a section title to the file
    with open(main_rtf,'a',encoding='utf-8') as f:
        f.write(f'\n{stitle}' + r'\fs48\par')

def add_sub_section_title(st:str,main_rtf:str):

    sstitle = rf'{{\f1\b\ul\cf11\fs40 {st}\par}}'

    #Add a sub section title to the file
    with open(main_rtf,'a',encoding='utf-8') as f:
        f.write(f'\n{sstitle}' + r'\fs48\par')

def add_code(code:str,main_rtf:str):

    script = ('\n'+ r'\fs24' + r'\par'+ '\n'+code + r'\par\par')

    #Add a code box to the file
    with open(main_rtf,'a',encoding='utf-8') as f:
        f.write(f'\n{script}')

def add_dot(l:str,main_rtf:str):

    dot = '\n'+ r'\fs24' + rf'{{\f1\b\cf7\u9670     }}{{\f1{correct_(l)}\par}}' + r'\par'

    #Add a text line to the file
    with open(main_rtf,'a',encoding='utf-8') as f :
        f.write(f'\n{dot}')

def new_page(main_rtf:str):

    #Jump page in the rtf file
    with open(main_rtf,'a',encoding='utf-8') as f :
        f.write(r'\page')

def close_rtf(main_rtf:str):

    #Add '}'  at the end to close the rtf file
    with open(main_rtf,'a',encoding='utf-8') as f :
        f.write(r'}')


if __name__=='__main__':
    main()
