def my_func1(num_1,num_2):
    return num_1**num_2

def my_func2(num_1,num_2):
    degree = -1
    result = 1
    while degree>=num_2:
        result /= num_1
        degree -=1
    return result

print(my_func1(6,-1))
print(my_func2(6,-1))