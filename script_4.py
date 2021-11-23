my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('script_4.txt', 'r') as file_obj:
    result = ''
    content = file_obj.readlines()
    for i in range(len(content)):
        string = content[i].replace(content[i].split()[0], my_dict.get(content[i].split()[0]))
        result += string
    with open('script_4_2.txt', 'wb') as file_obj_2:
        file_obj_2.write(result.encode('utf-8'))
