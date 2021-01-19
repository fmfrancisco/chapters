# Divide by zero
try:
    x = 5 / 0
except:
    print("Error dividing by zero")


# Invalid number conversion
try:
    x = int("fred")
except:
    print("Error converting fred to a number")


number_entered = False
while not number_entered:
    number_string = input("Enter an integer: ")
    try:
        n = int(number_string)
        number_entered = True
    except:
        print("Error, invalid integer")

    
# Error opening file
try:
    my_file = open("myfile.txt")
except:
    print("Error opening file")


try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(e)