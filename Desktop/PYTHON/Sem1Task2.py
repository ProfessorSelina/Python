# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def read_data(str):
    return int(input(str))
def sum_digit(num1):
    res = num1 % 10 + num1 // 10 % 10 + num1 // 100 % 10
    return res
num = read_data("Введите трехзначное число: ")
sum = sum_digit(num)
print(f"Сумма чисел трехзначного числа - {num} равна: {sum}")
