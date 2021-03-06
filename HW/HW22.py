from string import digits
from string import ascii_uppercase

x = digits + ascii_uppercase


def convert(num, system):
    str1 = []
    while num:
        str1.insert(0, x[num % system])
        num //= system
    str1 = ''.join(str1)
    return str1


n = int(input('Number: '))
s = int(input('System: '))

f = convert(n, s)
print('Result:', f)
