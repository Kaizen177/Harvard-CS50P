
import pytest

import fuel

def test_convert():

    assert fuel.convert('1/4') == 25
    assert fuel.convert('4/7') == 57
    assert fuel.convert('0/4') == 0
    assert fuel.convert('4/4') == 100

    with pytest.raises(ValueError):

        fuel.convert('7/4')
        fuel.convert('#/#')
        fuel.convert('g/g')
        fuel.convert(',/,')

    with pytest.raises(ZeroDivisionError):

        fuel.convert('1/0')
        fuel.convert('0/0')

def test_gauge():

    assert fuel.gauge(25)=='25%'
    assert fuel.gauge(98)=='98%'
    assert fuel.gauge(2)=='2%'
    assert fuel.gauge(99)=='F'
    assert fuel.gauge(100)=='F'
    assert fuel.gauge(1)=='E'
    assert fuel.gauge(0)=='E'




