class MyException(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = input('Введите делимое: ')
    b = input('Введите делитель: ')
    if int(b) == 0:
        raise MyException('b should be <> 0')
    else: print(int(a)/int(b))
except MyException as text:
    print(text)

print('program continue')
