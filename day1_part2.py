arr1, arr2 = [], []

with open('input.txt') as inputFile:
    for line in inputFile:
        inputs = line.split('   ')
        arr1.append(int(inputs[0]))
        arr2.append(int(inputs[1]))

memo = {}
for i in arr2:
    if memo.get(i) is None:
        memo[i] = 1
    else:
        memo[i]+=1

ans = 0

for i in arr1:
    if memo.get(i) is not None:
        ans += memo[i] * i

print(ans)
