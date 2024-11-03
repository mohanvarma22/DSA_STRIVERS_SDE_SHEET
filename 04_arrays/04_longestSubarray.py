from typing import List

def solve(a: List[int]) -> int:
    maxx = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 0:
                maxx = max(maxx, j-i+1)
    return maxx

if __name__ == "__main__":
    a = [9, -3, 3, -1, 6, -5]
    print(solve(a))


#for sum == 0
'''
from typing import List
def maxLen(A: List[int], n: int) -> int:
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(n):
        sum += A[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi

'''


#for sum == k
'''
from typing import List
def maxLen(A: List[int], n: int) -> int:
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(n):
        sum += A[i]
        if sum == k:
            maxi = i + 1
        else:
            if (sum-k) in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi
'''