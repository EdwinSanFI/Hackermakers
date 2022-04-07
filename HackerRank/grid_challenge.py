# def gridChallenge(grid):
#     grid2 = []
#     grid3 = []
#     j = 0
#     while j != len(grid[0]):
#         # print("Longitud: ",len(grid))
#         print("j: ",j)
#         for i in range(len(grid)):
#             print(grid[i][j])
#             grid[i] =sorted(grid[i])
#             grid2.append(grid[i][j])
#         j+=1
#         grid3 = grid2[len(grid2)-len(grid):]
#         print(grid3)
#         print(sorted(grid3))
#         if grid3 == sorted(grid3):
#             grid3.append('YES')
#         else:
#             grid3.append('NO')

#     print("Longitud: ",len(['123','456','789','123','456','789','123','456','789']))
#     print("Longitud2: ",len(['123456789','234567890']))
#     if 'NO' in grid3:
#         return 'NO'
    # else:
    #     return 'YES'


# def gridChallenge(grid):
#     grid2 = []
#     grid3 = []
#     for j in range(len(grid)):
#         grid[j] =sorted(grid[j])
#         if len(grid) < len(grid[j]):
#             for i in range(len(grid[j])):
#                 grid2.append(grid[j][i]) #No mover
#                 grid3 = grid2[len(grid2)-len(grid):]
#                 if grid3 == sorted(grid3):
#                     grid3.append('YES')
#                 else:                    
#                     grid3.append('NO')  
#         else: 
#             for i in range(len(grid[j])):
#                 grid2.append(grid[j][i]) #No mover
#                 grid3 = grid2[len(grid)-len(grid2):]     
#                 if grid3 == sorted(grid3):
#                     grid3.append('YES')
#                 else:
#                     grid3.append('NO')

#     if 'NO' in grid3:
#         return 'NO'
#     else:
#         return 'YES'

def gridChallenge(grid):
    grid2 = []
    grid3 = []
    grid4 = []
    # Acomoda las columnas
    for i in range(len(grid)):
            grid[i] =sorted(grid[i])
    #
    if len(grid) <= len(grid[0]):
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                grid2.append(grid[j][i])
            grid3 = grid2[len(grid2)-len(grid):]
            if grid3 == sorted(grid3):
                grid4.append('YES')
            else:
                grid4.append('NO')
    #       
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid2.append(grid[i][j])
            grid3 = grid2[len(grid2)-len(grid):]
            if grid3 == sorted(grid3):
                grid4.append('YES')
            else:
                grid4.append('NO')

    if 'NO' in grid4:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    grid = ['sur','eyy','gxy']
    print(gridChallenge(grid))