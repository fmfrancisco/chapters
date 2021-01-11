for row in range(35):
    if row < 10:
        print('*', end=' ')
        if row == 9:
            print('')
    elif 9 < row <= 14:
        print('*', end=' ')
        if row == 14:
            print('')
    elif row > 14:
        print('*', end=' ')

print('\n\n')

for row in range(10):
    print('*', end=' ')
print()
for row in range(5):
    print('*', end=' ')
print()
for row in range(20):
    print('*', end=' ')

print('\n\n')
for row in range(10):
    for column in range(10):
        print('*', end=' ')
    print()

print()

for row in range(10):
    for column in range(5):
        print('*', end=' ')
    print()

print()

for row in range(5):
    for column in range(20):
        print('*', end=' ')
    print()

print()

for row in range(10):
    for column in range(10):
        print(column, end=' ')
    print()

print()

for row in range(10):
    for column in range(10):
        print(row, end=' ')
    print()

print()
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9

for row in range(10):
    for column in range(row+1):
        print(column, end=' ')
    print()

print()
# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0

for row in range(10):
    # No primeiro laço o código abaixo será "ignorado", pois a variável 'i' está igual a zero
    for space in range(row):
        print('   ', end='')
    for j in range(10 - row):
        print(f'{j:<3}', end='')
    print()

print()
# 1   2   3   4   5   6   7   8   9
# 2   4   6   8  10  12  14  16  18
# 3   6   9  12  15  18  21  24  27
# 4   8  12  16  20  24  28  32  36
# 5  10  15  20  25  30  35  40  45
# 6  12  18  24  30  36  42  48  54
# 7  14  21  28  35  42  49  56  63
# 8  16  24  32  40  48  56  64  72
# 9  18  27  36  45  54  63  72  81

for row in range(1, 10):
    x = row
    for column in range(1, 10):
        print(f'{row:>3}', end=' ')
        row += x
    print()
print()
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:>3}', end=" ")
    print()
print()
empty = 20
for i in range(1, 10):
    print(' ' * empty, end='')
    for j in range(1, i):
        print(j, end=' ')
    for k in range(i, 0, -1):
        print(k, end=' ')
    empty -= 2
    print()
print()

for i in range(10):
    # Print leadin spaces
    for j in range(10-i):
        print(' ', end=' ')
    # Count up
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(i-1, 0, -1):
        print(j, end=' ')
    print()

for i in range(10):
    for j in range(10 - i):
        print(' ', end=' ')
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    print()

for i in range(1, 9):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(9-i):
        print(j+1, end=' ')
    print()

print('-' * 40)

for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

for i in range(10):
    # Print leading spaces
    for j in range(i + 2):
        print(" ", end=" ")
    # Count down
    for j in range(1, 9 - i):
        print(j, end=" ")
    # Next row
    print()

print('-' * 40)

for i in range(10):
    for j in range(10 - i):
        print(' ', end=' ')
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    print()
for i in range(1, 9):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(1, 10 - i):
        print(j, end=' ')
    for j in range(8 - i, 0, -1):
        print(j, end=' ')
    print()