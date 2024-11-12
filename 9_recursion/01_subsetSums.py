from typing import List

def subsetSums(arr: List[int], n: int) -> List[int]:
    ans = []
    
    # Helper function to calculate all subset sums
    def helper(ind: int, sum: int):
        if ind == n:
            ans.append(sum)
            return
        helper(ind + 1, sum + arr[ind])  # Include current element
        helper(ind + 1, sum)              # Exclude current element

    # Start recursion from index 0 with initial sum 0
    helper(0, 0)
    
    ans.sort()  # Sort the sums
    return ans

if __name__ == "__main__":
    arr = [3, 1, 2]
    ans = subsetSums(arr, len(arr))
    
    print("The sum of each subset is")
    for sum in ans:
        print(sum, end=" ")
    print()
