months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
n = int(input('Enter a month number: '))

n *= 3

print(months[n - 3:n])

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(ord(c), end=' ')

print()

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end='')

print()

encrypted_text = ''
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text +  c2
print(encrypted_text)

plain_text = ''

for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)
