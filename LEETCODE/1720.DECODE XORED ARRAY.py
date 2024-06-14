class Solution:
    def decode(self,A: list[int], first: int) -> list[int]:
        ans=[first]
        n=len(A)
        for i in range(n):
            a=ans[-1]^A[i]
            ans.append(a)
        return ans
