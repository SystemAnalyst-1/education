class MyException(Exception):
    def __init__(self, text):
        self.text = text


try:
    b = []
    while True:
        a = input('Введите элемент: ')
        if a == 'stop':
            break
        if not a.isdigit():
            raise MyException('a should be a number')
        else:
            b.append(int(a))

except MyException as text:
    print(text)

print(b)
