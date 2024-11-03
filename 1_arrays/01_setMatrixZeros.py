from typing import List
# brute force approach
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#     
#         n=len(matrix)
#         m=len(matrix[0])
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     self.markRows(matrix,n,m,i)
#                     self.markColumns(matrix,n,m,j)
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == -1:
#                     matrix[i][j] = 0
#         return matrix
    
#     def markRows(self,matrix: List[List[int]],n,m,i) -> None:
#         for j in range(m):
#             if matrix[i][j] != 0:
#                 matrix[i][j] = -1

#     def markColumns(self,matrix: List[List[int]],n,m,j) -> None:   
#         for i in range(n):
#             if matrix[i][j] != 0:
#                 matrix[i][j] = -1


#BETTER APPROACH USING EXTRA SPACE
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         n=len(matrix)
#         m=len(matrix[0])
#         row=[0]*n
#         col=[0]*m
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     row[i]=1
#                     col[j]=1
#         for i in range(n):
#             for j in range(m):
#                 if row[i] or col[j]:
#                     matrix[i][j] = 0
#         return matrix  

#optimal code time complexity = O(m*n) spacecomplexity = O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n=len(matrix)
        m=len(matrix[0])
        col0=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0 = 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]!=0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
        return matrix
                    

    

        
    

matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
solution.setZeroes(matrix)

print(matrix)