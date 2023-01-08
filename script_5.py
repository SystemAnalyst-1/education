from functools import reduce


def mult_num(prev, curr):
    return prev * curr


num_list = [i for i in range(100, 1001) if i % 2 == 0]
print(num_list)

result = reduce(mult_num, num_list)
print(result)
