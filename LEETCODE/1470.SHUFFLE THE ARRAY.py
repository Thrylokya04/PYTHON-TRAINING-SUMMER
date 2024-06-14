class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        answer=[]
        for i in range(0,n):
            answer.append(nums[i])
            answer.append(nums[i+n])
        return answer
