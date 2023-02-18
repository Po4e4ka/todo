attempts = 100
excepted_attempts = 3

for i in range(100):
    try:
        numbers_range = int(input("Введите, до какого числа считать: "))
    except Exception as e:
        excepted_attempts -= 1
        if excepted_attempts == 0:
            print("Превышено количество ошибок ввода подряд. Проверьте настройки клавиатуры. Выход из программы.")
            exit()
        print(f"Ошибка ввода. Необходимо ввести целое число. Осталось {excepted_attempts} попытки")
        continue

    var_sum = 0   # Не называем переменный зарезервированными словами
    for num in range(numbers_range):
        # if num % 3 == 0 and num % 5 == 0:
        #     var_sum += num * 2
        if num % 3 == 0:
            var_sum += num
        if num % 5 == 0:
            var_sum += num

    # var_sum = sum(list(range(0, numbers_range, 3)) + list(range(0, numbers_range, 5)))

    print(f"Итоговая сумма: {var_sum}")

    for a in range(100):
        exit_question = input("Желаете продолжить работу в программе? (y/n)")
        if exit_question == "y":
            break
        elif exit_question == "n":
            print("Выход из программы. До свидания!")
            exit()
        else:
            print("Неизвестная команда. Нажмите 'y' для продолжения работы или 'n' для выхода из программы.")

