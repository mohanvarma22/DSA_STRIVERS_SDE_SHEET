#brute force same as prev sum but here extra space is used and extra steps are included

'''okokka level of recursion lo okokka size of array possibilites
anni create aytay
 TC -> 2 pow n * n
 SC -> O(2 pow n) * O(k)
 def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ds = []


        def findSubsets(ind: int):
            ans.append(ds[:])
            for i in range(ind, len(nums)):
                if i != ind and nums[i] == nums[i - 1]:
                    continue
                ds.append(nums[i])
                findSubsets(i + 1)
                ds.pop()
        nums.sort()
        findSubsets(0)
        return ans




if __name__ == "__main__":
    nums = [1, 2, 2]
    obj = Solution()
    ans = obj.subsetsWithDup(nums)
    print("The unique subsets are ")
    print(*ans)

'''