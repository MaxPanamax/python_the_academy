try:
    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))
    numbers_list = [i for i in range(first_number, second_number + 1)] if first_number <= second_number else [i for i in range(second_number, first_number + 1)]

    print()
    
    for i in numbers_list:
        if not i % 3 and i % 5:
            print("Fizz")
        elif i % 3 and not i % 5:
            print("Buzz")
        elif not i % 3 and not i % 5:
            print("Fizz Buzz")
        else:
            print(i)

except ValueError:
    print("Введите корректные данные !!!")