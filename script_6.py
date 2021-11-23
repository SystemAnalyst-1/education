with open('script_6.txt', 'r', encoding='utf_8') as file_obj:
    content = file_obj.readlines()
    result = {}
    for i in range(len(content)):
        sum = 0
        line = content[i].split()
        for x in range(1, len(line)):
            num = ''
            for y in range(len(line[x])):
                if (line[x][y].isnumeric()):
                    num += line[x][y]
            if (num.isdigit()):
                sum += int(num)
        result[line[0]] = sum
    print(result)
