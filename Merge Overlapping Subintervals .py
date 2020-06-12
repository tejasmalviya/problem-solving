'''
Question:
    https://leetcode.com/problems/merge-intervals/submissions/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None
        
        intervals.sort(key= lambda x:x[0])
        
        ans=[]
        ans.append(intervals[0])
        
        for curr in intervals[1:]:
            if ans[-1][1]>=curr[0]:
                if ans[-1][1]>curr[1]:
                    continue
                else:
                    ans[-1][1]=curr[1]
            else:
                ans.append(curr)
                
        return ans
        
                        
