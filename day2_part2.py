
ans = 0
lent = 0

def jalo(levels):
    works = True
    for i in range(len(levels) - 1):
        difference = levels[i+1] - levels[i]
        if (difference <= 0 or difference > 3) :
            #print("aqui",i)
            works = False
            

    if works:
        return True
    else :
        works = True
        for i in range(len(levels) - 1):
            difference = levels[i] - levels[i+1]
            if (difference <= 0 or difference > 3) :
                #print("aqui",i)
                works = False

        if works:
            return True
    
    return False

with open('input.txt') as inputFile:
    for line in inputFile:
        lent +=1
        levels_string = line.split(' ')
        levels = []
        for i in levels_string:
            levels.append(int(i))

        bandera = jalo(levels)

        if bandera:
            ans+=1
            continue

        for j in range(len(levels)):
            aux = levels.copy()
            aux.pop(j)
            bandera = jalo(aux)
            if (bandera):
                ans+=1
                break

        #print("mamo",levels)

print(lent, ans)
