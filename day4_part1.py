mat = []
with open('input.txt') as inputFile:
    for line in inputFile:
        mat.append(line[:-1])

def busqueda(mat, _i, _j):
    N = len(mat)
    M = len(mat[0])
    word = "XMAS"
    directions_i = [-1,-1,-1,0,0,1,1,1]
    directions_j = [-1,0,1,-1,1,-1,0,1]

    #Horizontal 
    cont = 0
    for i in range(len(directions_i)):
        jalo = True
        for j in range(4):
            new_i = _i + (directions_i[i]*j)
            new_j = _j + (directions_j[i]*j)
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >=M:
                jalo = False
                break

            try:
                if mat[new_i][new_j] != word[j]:
                    jalo = False
                    break
            except:
                print(new_i, new_j, j)
        
        if jalo:
            cont += 1
    
    return cont

n = len(mat)
m = len(mat[0])

ans = 0

for row in range(n):
    #print(mat[row])
    for col in range(m):
        test = busqueda(mat, row, col)
        if test:
            #print(row,col)
            ans += test

print(ans)
