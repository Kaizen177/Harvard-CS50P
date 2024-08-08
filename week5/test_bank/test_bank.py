import pytest

from bank import value

def testing():

    assert value('hello world')==0
    assert value('Hello world') == 0
    assert value('hggg')==20
    assert value('ghh ,00')==100
    assert value('daaamn')==100
    assert value('ghello world')==100
    assert value('da333,,aamn')==100






