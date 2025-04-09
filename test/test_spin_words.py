import spin_words

def test_spin_words():
    assert (spin_words.spin_words("Welcome") == "emocleW")
    assert (spin_words.spin_words("I go home") == "I go home")
    assert (spin_words.spin_words("Please give me a pause") == "esaelP give me a esuap")

def test_no_spin_words():
    assert (spin_words.spin_words("Welcome") != "emocW")
    assert (spin_words.spin_words("I go home") != "I go emoh")
    assert (spin_words.spin_words("Please give me a pause") != "Please give me a pause")