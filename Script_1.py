import datetime


class Data:
    year = ''
    month =''
    day = ''

    def __init__(self, data):
        self.date = data
        self.data = data
        self.year = data.split('-')[0]
        self.day = data.split('-')[1]
        self.month = data.split('-')[2]


    @classmethod
    def get_mdy(cls):
        print(cls.day)
        print(cls.year)
        print(cls.month)
        return (1000 * int(cls.year)) + (10 * int(cls.month)) + int(cls.day)

    @staticmethod
    def check_date(date):
        data = date.split('-')
        if 0 < int(data[1]) < 13:
            print('Month is correct')
        else:
            print('Month is incorrect')
        if 0 < int(data[0]) < 32:
            print('day is correct')
        else:
            print('day is incorrect')


my_date = Data('2010-01-31')
my_date.check_date(my_date.date)
print(my_date.get_mdy())