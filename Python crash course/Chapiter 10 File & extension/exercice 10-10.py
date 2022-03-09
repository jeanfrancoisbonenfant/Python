filenames = ["book/alice.txt", "book/sherlock.txt", "book/moby_dick.txt"]

for filename in filenames:
    number_the = 0
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        words = content.split()
        number_words = len(words)
        for word in words:
            number_the += word.lower().count('the')
        print(f"The book {filename} contains {number_words} words and {number_the} 'the' in the text.")