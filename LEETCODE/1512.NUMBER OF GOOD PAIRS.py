class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hashmap={}
        res=0
        for number in nums:
            if number in hashmap:
                res += hashmap[number]
                hashmap[number] += 1
            else:
                hashmap[number]=1
        return res
