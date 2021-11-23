with open('script_2.txt','r') as file_obj:
    content = file_obj.readlines()
    print(len(content))
    for i in range(len(content)):
        print(f'{i} = {len(content[i])}')