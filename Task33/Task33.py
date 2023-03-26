# Задача 33.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# def max_replace_min():

def max_on_min(input_list: list):
    min_grade = input_list[0]
    max_grage = input_list[0]
    for i in range(len(input_list)):
        if input_list[i] > max_grage:
            max_grage = input_list[i]
        if input_list[i] < min_grade:
            min_grade = input_list[i]
    for i in range(len(input_list)):
        if input_list[i] == max_grage:
            input_list[i] = min_grade

input_list = []
list_len = int(input('Введите количество элементов в списке: '))
element_count = 1
for _ in range(list_len):
    input_list.append(int(input(f'Введите {element_count} число: ')))
    element_count = element_count + 1
print(input_list)
max_on_min(input_list)
print(input_list)





