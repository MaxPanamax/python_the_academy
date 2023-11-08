text = input("Введите текст: ").lower().split()
some_words = input("Введите список слов через пробел: ").lower().split()

for i in some_words:
    while i in text:
        text[text.index(i)] = i.upper()

print(" ".join(text))