
import pytest

from plates import is_valid

def test_valid():

    assert is_valid('CS50') == True
    assert is_valid('cs50') == True
    assert is_valid('cscc50') == True
    assert is_valid('Cs5000') == True
    assert is_valid('abcabc') == True
    assert is_valid('vvv333') == True
    assert is_valid('c5g00') == False
    assert is_valid('C500') == False
    assert is_valid('c12345') == False
    assert is_valid('cs0123') == False
    assert is_valid('cc123456') == False
    assert is_valid('5cc00') == False
    assert is_valid('cc10c0') == False
    assert is_valid('123') == False
    assert is_valid('cc#') == False



