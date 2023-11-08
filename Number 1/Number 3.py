text = input("Введите текст: ").split()
count = 0

for i in text:
    if "." in i or "!" in i or "?" in i:
        count += 1

print(f"Количество предложений в тексте равняется: {count}")