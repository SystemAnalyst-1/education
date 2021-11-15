from itertools import count, cycle

for i in count(3):
    print(i)
    if i == 10:
        break
        
print("Second script")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
counter = 0
for i in cycle(my_list):
    print(i)
    counter += 1
    if counter == len(my_list):
        break
