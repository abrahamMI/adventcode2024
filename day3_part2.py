import re

ans = 0

def multiplyFunction(s):
    aux = 0
    operations = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",s)

    for operation in operations:
        [number_1, number_2] = operation.split(",")
        number_1 = number_1[4:]
        number_2 = number_2[0:-1]

        aux += int(number_1) * int(number_2)

    return aux

unique_line = ""

with open('input.txt') as inputFile:
    for line in inputFile:
        unique_line += line

do_lines = re.split("do\(\)",unique_line)
for do_line in do_lines:
    dont_lines = re.split("don't\(\)",do_line)
    ans += multiplyFunction(dont_lines[0])

print(ans)
