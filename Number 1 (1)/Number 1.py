try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    numbers_list = [i for i in range(first_number, second_number + 1)] if first_number <= second_number else [i for i in range(second_number, first_number + 1)]

    print()

    print(f"Числа кратные 7: {[i for i in numbers_list if not i % 7]}\n") if len([i for i in numbers_list if not i % 7]) else print("Чисел кратных 7 не существует !!!\n")

except ValueError:
    print("Введите корректные данные !!!")