def division (arg_1, arg_2):
    if arg_2 == 0:
        print("Деление на 0 невозможно")
        return "Error"
    result = arg_1/arg_2
    return result

dividend = input("Введите делимое: ")
divider = input("Введите делитель: ")
print(f"Частное = {division(float(dividend),float(divider))}")
