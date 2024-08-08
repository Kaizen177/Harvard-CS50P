from jar import Jar
import pytest

def test_init():

    jar=Jar()
    assert jar==Jar(12,0)

def test_str():
    jar=Jar(5,3)
    assert str(jar)=='🍪🍪🍪'

def test_deposit():

    jar=Jar()
    jar.deposit(6)
    assert jar==Jar(12,6)

    with pytest.raises(ValueError):
        jar.deposit(7)

def test_withdraw():

    jar=Jar()
    jar.deposit(5)
    jar.withdraw(3)

    assert jar==Jar(12,2)

    with pytest.raises(ValueError):
        jar.withdraw(3)







