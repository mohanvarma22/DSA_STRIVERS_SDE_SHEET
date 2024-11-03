# def longest(arr):
#     count=1
#     arr.sort()
#     max_count=1
#     for i in range(len(arr)-1):
#         if arr[i+1] == arr[i]:
#             continue
#         elif arr[i+1] - arr[i] ==1:
#             count +=1
#         else:
#             count = 1
#         max_count=max(count,max_count)
#     return max_count

def longestConsecutiveSequence(nums):
    # If the list is empty, there is no sequence
    if not nums:
        return 0

    # Convert the list to a set for quick lookups
    num_set = set(nums)
    longest_sequence = 0

    # Go through each number in the set
    for num in num_set:
        # Check if 'num' is the start of a sequence
        if num - 1 not in num_set:  # Only start counting if 'num' is the beginning of a sequence
            current_num = num
            current_streak = 1

            # Count the length of the current sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest sequence found so far
            longest_sequence = max(longest_sequence, current_streak)

    return longest_sequence

# Example usage
a = [100, 200, 1, 2, 3, 4]
ans = longestConsecutiveSequence(a)
print(ans)  # Output: 4

# arr = [0,3,7,2,5,8,4,6,0,1]
# print(longest(arr))