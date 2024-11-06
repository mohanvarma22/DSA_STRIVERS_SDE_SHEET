#i<j and a[i]>2*arr[j]
#brute force nested loops

'''optimal
[6 13 21 25]  [1 2 3 4 4 5 9 11 13]
6->[1,2]
13->[1,2,3,4,4,5]
21->[1,2,3,4,4,5,9]
25->[1 2 3 4 4 5 9 11]
see here we can see a pattern

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr, low, mid, high):
            temp = []  # temporary array
            left = low  # starting index of left half of arr
            right = mid + 1  # starting index of right half of arr

            # storing elements in the temporary array in a sorted manner
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1

            # if elements on the left half are still left
            while left <= mid:
                temp.append(arr[left])
                left += 1

            # if elements on the right half are still left
            while right <= high:
                temp.append(arr[right])
                right += 1

            # transferring all elements from temporary to arr
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def countPairs(arr, low, mid, high):
            right = mid + 1
            cnt = 0
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt

        def mergeSort(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            cnt = mergeSort(arr, low, mid)  # left half
            cnt += mergeSort(arr, mid + 1, high)  # right half
            cnt += countPairs(arr, low, mid, high)  # count reverse pairs
            merge(arr, low, mid, high)  # merging sorted halves
            return cnt

        return mergeSort(nums, 0, len(nums) - 1)
'''