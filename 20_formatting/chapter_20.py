import random

for i in range(10):
    x = random.randrange(100000)
    print(f'{x:6,}')

x = 5
y = 66
z = 777
print(f'A - {x} \nB - {y} \nC - {z}')

for hours in range(1, 13):
    for minutes in range(0, 60):
        print(f'Time: {hours:02}:{minutes:02}')
    