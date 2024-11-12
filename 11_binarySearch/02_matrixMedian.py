#Brute force
'''easiest way entante you can store the matrix elements
in a list and sort it and then return the (m*n)//2th element'''
'''                                    
def median(matrix, m, n):
    lst = []

    # Traverse the matrix and copy the elements to the list:
    for i in range(m):
        for j in range(n):
            lst.append(matrix[i][j])

    # Sort the list:
    lst.sort()
    return lst[(m * n) // 2]

matrix = [
    [1, 2, 3, 4, 5],
    [8, 9, 11, 12, 13],
    [21, 23, 25, 27, 29]
]
m = len(matrix)
n = len(matrix[0])
ans = median(matrix, m, n)
print("The median element is:", ans)
                                    
                                '''

                                    #video or description sarigga chaduvu malli                    
def upperBound(arr, x, n):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for a smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

def countSmallEqual(matrix, m, n, x):
    cnt = 0
    for i in range(m):
        cnt += upperBound(matrix[i], x, n)
    return cnt

def median(matrix, m, n):
    low = float('inf')
    high = float('-inf')

    # point low and high to the right elements
    for i in range(m):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][n - 1])

    req = (n * m) // 2
    while low <= high:
        mid = (low + high) // 2
        smallEqual = countSmallEqual(matrix, m, n, mid)
        if smallEqual <= req:
            low = mid + 1
        else:
            high = mid - 1

    return low

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
    m = len(matrix)
    n = len(matrix[0])
    ans = median(matrix, m, n)
    print("The median element is:", ans)
                                    
                                