
str_var = "hello, how are you!?"
char_count = 0
char_index_list = []
char_find = input('Введите букву: ')
for index, char in enumerate(str_var):
    if char == char_find:
        char_index_list.append(str(index))
        char_count += 1

print(f"Идексы, где есть буква '{char_find}': {char_index_list}")





# str_var = "hello, how are you!?"
# char_count = 0
# char_find = input('Введите букву: ')
# for char in str_var:
#     if char == char_find:
#         char_count += 1
# print(f'Количество = {char_count}')

# ask= '\nХотите повторить? (y/n): '
# for _ in range(1000):
#     n = None
#     for i in range(3):
#         try:
#             n = int(input('Введите целое, положительное число: '))
#         except Exception as e:
#             print('Необходимо ввести ЧИСЛО')
#             continue
#
#         if n <= 0:
#             print('Необходимо ввести ПОЛОЖИТЕЛЬНОЕ число')
#             continue
#
#         if i == 2:
#             print('\nОшибка ввода данных')
#             n = None
#
#         break
#
#     if n is None:
#         if input(ask) == 'y':
#             continue
#         else:
#             break
#
#     sum_list = [sum(range(0, n, 3)),
#                 sum(range(0, n, 5))]
#
#     print(f'\nСумма чисел кратных 3 и 5 равна {sum(sum_list)}')
#
#     if input(ask) == 'y':
#         continue
#     else:
#         break
#
# print('До свидания!!')
