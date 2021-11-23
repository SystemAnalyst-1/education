with open('script_3.txt', 'r') as file_obj:
    content = file_obj.readlines()
    sum = 0
    for i in range(len(content)):
        line = content[i].split()
        if int(line[1]) < 20:
            print(line[0])
        sum += int(line[1])
    print(sum / len(content))
