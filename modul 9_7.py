# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает
# "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    print('Это составное число')
                    break
                else:
                    print('Это простое число')
                    break
        return number
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
result_2  = sum_three(1, 1, 10)
print(result_2)
