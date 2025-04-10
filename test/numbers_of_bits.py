def count_bits(n):
    count = 0
    bi = bin(n)
    for symbol in bi:
        if symbol == "1":
            count += 1
    return count

assert(count_bits(1234) == 5)