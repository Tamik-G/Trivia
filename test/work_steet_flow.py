quotes = []
authors = []

with open('street_flow.txt') as f:
    for line in f.readlines():
        if line[0].isdigit():
            quotes.append(line[2: -1]) # -1 убирает перевод на новую строку
        elif line[0] == '-':
            authors.append(line[2: -1])

with open("new_street_flow.txt", "w") as f:
    for quote, author in zip(quotes[::-1], authors[::-1]):
        f.write(f"Однажды {author} сказал:\n {quote}\n\n ")