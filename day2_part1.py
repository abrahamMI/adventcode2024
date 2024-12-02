
ans = 0
lent = 0

with open('input.txt') as inputFile:
    for line in inputFile:
        lent +=1
        levels_string = line.split(' ')
        levels = []
        for i in levels_string:
            levels.append(int(i))

        works = True
        for i in range(len(levels) - 1):
            difference = levels[i+1] - levels[i]
            if (difference <= 0 or difference > 3) :
                #print("aqui",i)
                works = False
                

        if works:
            ans+=1
        else :
            works = True
            for i in range(len(levels) - 1):
                difference = levels[i] - levels[i+1]
                if (difference <= 0 or difference > 3) :
                    #print("aqui",i)
                    works = False

            if works:
                ans+=1

        #print("mamo",levels)

print(lent, ans)
