arr1, arr2 = [], []

with open('testing.txt') as inputFile:
    for line in inputFile:
        inputs = line.split('   ')
        arr1.append(int(inputs[0]))
        arr2.append(int(inputs[1]))

arr1.sort()
arr2.sort()
ans = 0

for i in range(len(arr1)):
    ans += abs(arr1[i] - arr2[i])
  
print(ans)
