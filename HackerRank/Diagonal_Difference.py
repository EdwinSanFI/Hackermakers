def diagonalDifference(arr):
    primaryDiagoonal = 0
    secondaryDiagoonal = 0
    j = len(arr)
    for i in range(len(arr)):
        primaryDiagoonal += arr[i][i]
        j -= 1
        secondaryDiagoonal += arr[i][j]

    difference = primaryDiagoonal-secondaryDiagoonal
    return (difference*-1 if difference < 0 else difference)

if __name__ == '__main__':
    test7 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(test7)
    print(result)
    # Expected output: 15

    # test3 = [[-10, 3, 0, 5, -4], [2, -1, 0, 2, -8], [9, -2, -5, 6, 0], [9, -7, 4, 8, -2], [3, 7, 8, -5, 0]]
    # Expected output: 3

    # test5 = [[1,1,1],[1,1,1],[1,1,1]]
    # Expected output: 0

    # test4 = [[6,8],[-6,9]]
    # Expected output: 13