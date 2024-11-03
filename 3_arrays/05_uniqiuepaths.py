#brute force solution tc and sc is exponential
# def countPaths(i,j,n,m):
#     if i == n-1 and j == m-1:
#         return 1
#     if i>=n or j>=m:
#         return 0
#     else:
#         return countPaths(i+1,j,n,m) + countPaths(i,j+1,n,m)


# print(countPaths(0,0,3,7))

#optimal have to convert the recursive code to dp code


def countPaths(i,j,n,m,dp=None):
    if dp is None:
        dp = {}
    if i == n-1 and j == m-1:
        return 1
    if i>=n or j>=m:
        return 0
    if (i,j) in dp:
        return dp[(i,j)]
    dp[(i,j)] = countPaths(i+1,j,n,m,dp) + countPaths(i,j+1,n,m,dp)
    return dp[(i,j)]


print(countPaths(0,0,3,7))