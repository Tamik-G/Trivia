from sum_of_digits import digital_root

def test_sum_of_digits():
    assert (digital_root(16) == 7)
    assert (digital_root(9) == 9)
    assert (digital_root(942) == 6)
    assert (digital_root(132189) == 6)
    assert (digital_root(493193) == 2)

def test_no_sum_of_digits():
    assert (digital_root(16) != 2)
    assert (digital_root(942) != 9)
    assert (digital_root(132189) != 1)
    assert (digital_root(493193) != 78)