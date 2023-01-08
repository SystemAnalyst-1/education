list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
with open('script_5.txt', 'w') as file_obj:
    for i in range(len(list_num)):
        print(list_num[i], file=file_obj, end=' ')

with open('script_5.txt', 'r') as file_obj:
    content = file_obj.readline()
    sum = 0
    list = content.split()
    for i in range(len(list)):
        sum+= int(list[i])
    print(sum)
