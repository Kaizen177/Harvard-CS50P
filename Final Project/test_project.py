import pytest
import requests_mock
from project import *
from unittest.mock import patch

mock_lectures_html = '''
<ol>
    <li>Lecture 0</li>
    <li>Lecture 1</li>
    <li>Lecture 2</li>
</ol>
'''

mock_sections_html = '''
<h2 id="section1">Section 1</h2>
<p>Paragraph 1</p>
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>
<h2 id="section2">Section 2</h2>
<p>Paragraph 2</p>
<ul>
    <li>Item 3</li>
    <li>Item 4</li>
</ul>
<h2 id="section3">Section 3</h2>
<p>Paragraph 3</p>
<ul>
    <li>Item 5</li>
    <li>Item 6</li>
</ul>
<h3 id="subsection1">Subsection 1</h3>
<ul>
    <li>Subitem 1</li>
</ul>
'''

def test_get_lectures():
    with requests_mock.Mocker() as m:
        m.get('https://cs50.harvard.edu/python/2022/', text = mock_lectures_html)
        lectures = get_lectures('https://cs50.harvard.edu/python/2022/')
        assert lectures == ['Lecture 0', 'Lecture 1', 'Lecture 2']


def test_get_sections_content():

    '''
        [get_sections_content] function use both [ul_to_tuples] and [add_h3] functions to work
        If [ul_to_tuples] or [add_h3] fail the test, [get_sections_content] will fail too
        So [test_get_sections_content] test all 3 functions together not only [get_sections_content] function

    '''
    with requests_mock.Mocker() as m:
        m.get('https://cs50.harvard.edu/python/2022/notes/0/', text = mock_sections_html)
        content1, titles1 = get_sections_content(0, [])
        assert titles1 == ['section 1', 'section 2','section 3']
        assert content1 == [
            [('Section 1', 'stitle'), ('Paragraph 1', 'p'), ('Item 1', 'li'), ('Item 2', 'li')],
            [('Section 2', 'stitle'), ('Paragraph 2', 'p'), ('Item 3', 'li'), ('Item 4', 'li')],
            [('Section 3', 'stitle'), ('Paragraph 3', 'p'), ('Item 5', 'li'), ('Item 6', 'li'),
             ('Subsection 1', 'sstitle'), ('Subitem 1', 'li')]]

    with requests_mock.Mocker() as m:
        m.get('https://cs50.harvard.edu/python/2022/notes/0/', text = mock_sections_html)
        content2, titles2 = get_sections_content(0, ['Section 2'])
        assert titles2 == ['section 2']
        assert content2 == [
            [('Section 2', 'stitle'), ('Paragraph 2', 'p'), ('Item 3', 'li'), ('Item 4', 'li'),
             ]]
    with requests_mock.Mocker() as m:
        m.get('https://cs50.harvard.edu/python/2022/notes/0/', text = mock_sections_html)
        content1, titles1 = get_sections_content(0, ['Section 3','Section 1'])
        assert titles1 == ['section 1','section 3']
        assert content1 == [
            [('Section 1', 'stitle'), ('Paragraph 1', 'p'), ('Item 1', 'li'), ('Item 2', 'li')],
            [('Section 3', 'stitle'), ('Paragraph 3', 'p'), ('Item 5', 'li'), ('Item 6', 'li'),
             ('Subsection 1', 'sstitle'), ('Subitem 1', 'li')]]

def test_main():
    with requests_mock.Mocker() as m:
        m.get('https://cs50.harvard.edu/python/2022/', text = mock_lectures_html)
        m.get('https://cs50.harvard.edu/python/2022/notes/1/', text = mock_sections_html)
        with patch('sys.argv', ['project.py', '1']):
            main()

def test_no_arguments():
    with patch('sys.argv', ['project.py']):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert str(excinfo.value) == "No arguments provided.\nUsage : [1: all] or [1: LectureNumber 2: \"section1-section2-section3\" ...]\nIf sections not provided, all lecture sections will be printed."

def test_too_many_arguments():
    with patch('sys.argv', ['project.py', '1', '2', '3']):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert str(excinfo.value) == "Too many arguments.\nUsage : [1: all] or [1: LectureNumber 2: \"section1-section2-section3\" ...]\nIf sections not provided, all lecture sections will be printed."

def test_incorrect_first_argument():
    with patch('sys.argv', ['project.py', 'abc']):
        with pytest.raises(SystemExit) as excinfo:
            main()
        assert str(excinfo.value) == "Incorrect first argument\nUsage : [1: all] or [1: LectureNumber 2: \"section1-section2-section3\" ...]\nIf sections not provided, all lecture sections will be printed."
