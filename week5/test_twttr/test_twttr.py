import pytest

from twttr import shorten

def test_shorten():
    assert shorten('word')=='wrd'
    assert shorten('FACEBOOK')=='FCBK'
    assert shorten('twitter,')=='twttr,'
    assert shorten('twitter0,')=='twttr0,'

