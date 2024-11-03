import math
#3 types of questions
#1 print n rows of a pascal triangle
# optimal
def generateRow(row):
    ans = 1
    ansRow = [1]
    for col in range(1,row):
        ans*=(row-col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n):
    ans = []
    for row in range(1,n+1):
        ans.append(generateRow(row))
    return ans

print(pascalTriangle(5))

#2 print the element when rownum and colnum is given (call for r-1,c-1)(nCr)
# def nCr(n,r):
#     res=1
#     for i in range(r):
#         res=res*(n-i)
#         res=res// (i+1)
#     return res
# print(nCr(5,2))

#3 print the nth row of the triangle
# brute force
# for i in range(n):
#     nCr(n-1,r-1)

#optimal TC->O(N) SC->O(1)

# def pascalTriangle(n):
#     ans=1
#     print(ans,end = " ")
#     for i in range(1,n):
#         ans = ans * (n-i)
#         ans = ans//i
#         print(ans, end=" ")
#     # print()
# pascalTriangle(5)