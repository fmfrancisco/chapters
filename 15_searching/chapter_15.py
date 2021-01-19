file = open("/home/francisco/Documentos/GitHub/program_arcade_games/chapters/15_searching/super_villains.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

for name in name_list:
    print(name)

key = 'Morgiana the Shrew'

i = 0

while i < len(name_list) and name_list[i] != key:
    i += 1

if i < len(name_list):
    print(f'The name is at position {i}')
else:
    print('The name was not in the list.')


class Alien:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    

def has_property(my_alien):
    if my_alien.color.upper() == 'GREEN':
        return True
    else:
        return False


def check_if_one_item_has_property_v1(my_list):
    i = 0
    while i < len(my_list) and not has_property(my_list[i]):
        i += 1
    
    if i < len(my_list):
        return True
    else:
        return False


def check_if_one_item_has_property_v2(my_list):
    for item in my_list:
        if has_property(item):
            return True
    return False


def check_if_all_items_have_property(my_list):
    for item in my_list:
        if not has_property(item):
            return False
    return True


def get_matching_items(list):
    matching_list = []
    for item in list:
        if has_property(item):
            matching_list.append(item)
    return matching_list


alien_list = []
alien_list.append(Alien('Green', 42))
alien_list.append(Alien('Red', 42))
alien_list.append(Alien('Blue', 42))
alien_list.append(Alien('Purple', 42))

result = check_if_one_item_has_property_v1(alien_list)
print(f'Result of test check_if_one_item_has_property_v1: {result}')

result = check_if_one_item_has_property_v2(alien_list)
print(f'Result of test check_if_one_item_has_property_v2: {result}')

result = check_if_all_items_have_property(alien_list)
print(f'Result of test check_if_all_items_have_property: {result}')

result = get_matching_items(alien_list)
print(f'Number of items returned from test get_matching_items: {len(result)}')