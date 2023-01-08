def int_func(str):
    return str.capitalize()


str_in_lower = input("Введите строку: ").split()
result = ""
for str in str_in_lower:
    result += int_func(str)
    result += " "
print(result)