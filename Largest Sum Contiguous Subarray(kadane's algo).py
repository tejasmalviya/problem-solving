'''
Question:
    https://leetcode.com/problems/maximum-subarray/submissions/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if max(nums)<=0:
            return max(nums)
        
        maxx=0
        maxsofar=0
        
        for i in range(len(nums)):
            
            maxsofar+=nums[i]
            
            if maxsofar<0:
                maxsofar=0
                continue
            
            maxx=max(maxx,maxsofar)
        
        return maxx
