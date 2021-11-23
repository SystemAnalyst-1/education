import json

with open('script_7.txt', 'r') as file_obj:
    content = file_obj.readlines()
    my_dict = {}
    avg = 0
    count = 0
    for i in content:
        list = i.split()
        my_dict[list[0]] = int(list[2]) - int(list[3])
    for i in my_dict.values():
        if i > 0:
            avg += i
            count += 1

    my_dict['average_profit'] = avg / count
    with open('script_7_2.txt','w') as file_obj_2:
        json.dump(my_dict,file_obj_2)

