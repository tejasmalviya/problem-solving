'''
Question:
    https://www.interviewbit.com/problems/repeat-and-missing-number-array/
'''
class Solution:
    # @param A : tuple of integers
    # @return a list of integers=>[repeated numbers,missing number]
    def repeatedNumber(self, A):
        A=list(A)
        ans=[]
        for i in range(len(A)):
            if A[abs(A[i])-1]>0:
                A[abs(A[i])-1]=-A[abs(A[i])-1]
            else:
                ans.append(abs(A[i]))
        ans.append(A.index(max(A))+1)
        
        return ans
                
