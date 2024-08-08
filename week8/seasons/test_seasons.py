from seasons import convert


def test_date():

    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
