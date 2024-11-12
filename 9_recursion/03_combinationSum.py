#general ga one element one time ey pick cheyalante recursive call lo
#ind + 1 ki call chestam but in this case one element can
#be picked multiple times lo same ind ki call chesyyali

'''class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []


        def findCombination(ind: int, target: int):
            if ind == len(candidates):
                if target == 0:
                    ans.append(ds[:])
                return
            if candidates[ind] <= target:
                ds.append(candidates[ind])
                findCombination(ind, target - candidates[ind])
                ds.pop()
            findCombination(ind + 1, target)
        findCombination(0, target)
        return ans




if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    ans = obj.combinationSum(candidates, target)
    print("Combinations are: ")
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()
'''