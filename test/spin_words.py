def spin_words(sentence):
    words = sentence.split(' ')
    result = []
    otvet = []
    str = ''
    for word in words:
        if len(word) > 4:
            for letter in word:
                result.insert(0,letter)
        else:
            for letter in word:
                result.append(letter)
        str = ''.join(result)
        otvet.append(str)
        result.clear()
    str_otvet = ' '.join(otvet)
    return str_otvet
