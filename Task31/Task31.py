# Задача 31.
# Требуется найти N-e число Фибоначчи.
# Пример: Введено 7, Выдано 21 ( то есть 21 это 7-е число в числах Фибоначчи)

def fib(num):
	if num == 1:
		return 0
	if num == 2:
		return 1
	return fib(num - 1) + fib(num - 2)


print(fib(8))

# РЕШЕНИЕ С ПОМОЩЬЮ ЦИКЛА (Цикл всегда быстрее рекурсии)

# def fibonachi_iteration(serial_number):
#     first = 0
#     second = 1
#     if serial_number == 1:
#         return first
#     if serial_number == 2:
#         return second

#     count = 2

#     while serial_number != count:
#         third = first + second
#         first = second
#         second = third
#         count = count + 1
#     return third



# print(fibonachi_iteration(7))

# Замер Времени

# import time
#
# some_list = [random.randint(1, 1000000) for _ in range(1000000)]
#
# start = time.perf_counter()

# Тут код

# end = time.perf_counter()

# first_time = end - start


# start = time.perf_counter()

# Тут код

# end = time.perf_counter()

# second_time = end - start


# print(first_time / second_time)
