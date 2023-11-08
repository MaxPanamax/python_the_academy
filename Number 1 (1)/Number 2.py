try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    numbers_list = [i for i in range(first_number, second_number + 1)] if first_number <= second_number else [i for i in range(second_number, first_number + 1)]

    print()
    
    print(f"Все числа диапазона: {[i for i in numbers_list]}\n")

    print(f"Все числа диапазона в убывающем порядке: {[i for i in numbers_list[::-1]]}\n")

    print(f"Числа кратные 7: {[i for i in numbers_list if not i % 7]}\n") if len([i for i in numbers_list if not i % 7]) else print("Чисел кратных 7 не существует !!!\n")

    print(f"Количество чисел кратных 5: {len([i for i in numbers_list if not i % 5])}\n") if len([i for i in numbers_list if not i % 5]) else print("Чисел кратных 5 не существует !!!\n")

except ValueError:
    print("Введите корректные данные !!!")