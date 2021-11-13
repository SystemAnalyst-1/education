continuation = True
sum = 0
while continuation == True:
    num_str = input("Введите строку чисел: ")
    num_list = num_str.split()
    for num in num_list:
        if not num.isdigit():
            continuation = False
            break
        sum+= float(num)
    print(sum)