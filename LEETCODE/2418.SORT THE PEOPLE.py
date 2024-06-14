class Solution:
    def sortPeople(self,names:list[str],heights:list[int])->list[str]:
        ans=zip(heights,names)
        l=[]
        for i,j in sorted(ans):
            l.append(j)
        return l[::-1]
