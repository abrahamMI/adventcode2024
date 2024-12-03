import re

ans = 0

with open('input.txt') as inputFile:
    for line in inputFile:
        operations = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)",line)

        for operation in operations:
            [number_1, number_2] = operation.split(",")
            number_1 = number_1[4:]
            number_2 = number_2[0:-1]

            ans += int(number_1) * int(number_2)

            #print(number_1, number_2)

print(ans)
