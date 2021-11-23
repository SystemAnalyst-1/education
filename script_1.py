result = ''
content = input('Введите что нибудь')
while len(content)>0:
    result += content + '\n'
    content = input('Введите что нибудь')

with open('script_1.txt', 'w') as file_obj:
    print(result, file=file_obj)