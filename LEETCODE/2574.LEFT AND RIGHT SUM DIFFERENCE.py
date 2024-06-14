class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return ans
