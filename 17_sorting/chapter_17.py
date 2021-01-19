import random

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
print(my_list)
temp = my_list[0]
my_list[0] = my_list[2]
my_list[2] = temp
print(my_list)


def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
        
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


def print_list(my_list):
    for item in my_list:
        print(f'{item:3}', end=' ')
    print()


my_list = []
for i in range(10):
    my_list.append(random.randrange(100))

print_list(my_list)
selection_sort(my_list)
print_list(my_list)
