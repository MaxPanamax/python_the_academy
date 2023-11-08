text = input("Введите текст: ")

print(f"'{text.capitalize()}' является палиндромом") \
if "".join(text.lower().split()) == "".join(text[::-1].lower().split()) \
else print(f"'{text.capitalize()}' не является палиндромом")