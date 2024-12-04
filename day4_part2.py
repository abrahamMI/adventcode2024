mat = []
with open('input.txt') as inputFile:
    for line in inputFile:
        mat.append(line[:-1])

def busqueda(mat, _i, _j,word):
    N = len(mat)
    M = len(mat[0])
    directions_i = [-1,-1,0,1,1]
    directions_j = [-1,1,0,-1,1]

    jalo = True
    for i in range(len(word)):
        new_i = _i + directions_i[i]
        new_j = _j + directions_j[i]
        if new_i < 0 or new_i >= N or new_j < 0 or new_j >=M:
            jalo = False
            break

        try:
            if mat[new_i][new_j] != word[i]:
                jalo = False
                break
        except:
            print(new_i, new_j, j)
        
    if jalo:
        return 1
    
    return 0


n = len(mat)
m = len(mat[0])

ans = 0

for row in range(n):
    #print(mat[row])
    for col in range(m):
        test = 0
        test += busqueda(mat, row, col,"MSAMS")
        test += busqueda(mat, row, col,"MMASS")
        test += busqueda(mat, row, col,"SSAMM")
        test += busqueda(mat, row, col,"SMASM")
        if test:
            #print(row,col)
            ans += test

print(ans)
