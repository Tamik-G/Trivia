from numbers_of_bits import count_bits

def test_count_bits():
    assert (count_bits(1234) == 5)
    assert (count_bits(4) == 1)
    assert (count_bits(7) == 3)
    assert (count_bits(9) == 2)
    assert (count_bits(10) == 2)