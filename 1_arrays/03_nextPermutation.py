#[3,1,2] => 6 possible rearrangements 3!

#Brute force steps generate all sorted(learn properly from recursion playlist) => linear search => Next element

#optimal
#observations

'''1) longer prefix match find cheyali while reverse traversing
find a target value where a[i]<a[i+1]
2)again while reverse traversing find an minimum element which is
 greater than the target element
 3)place the remaining in sorted order'''
from typing import List

def nextGreaterPermutation(arr: List[int]) -> List[int]:
    n=len(arr)
    ind = -1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            ind = i
            break

    if ind == -1:
        arr.reverse()
        return arr

    for i in range(n-1,ind,-1):
        if arr[i]>arr[ind]:
            arr[i],arr[ind]=arr[ind],arr[i]
            break
    arr[ind+1:] = arr[ind+1:][::-1]
    return arr

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextGreaterPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")